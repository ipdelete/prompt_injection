import json
import logging
from datetime import datetime
from typing import Dict, List, Any
import re
from mock_llm_service import MockLLMService
from doc_tool import DocumentTool
from email_tool import EmailTool

class VulnerableAgent:
    def __init__(self, config):
        self.config = config
        self.email_tool = EmailTool(config.get('email', {}))
        self.doc_tool = DocumentTool(config.get('documents', {}))
        self.mock_llm = MockLLMService()
        self.security_logger = logging.getLogger('security')
        
        # Define available tools
        self.tools = {
            'send_email_tool': {
                'function': self.email_tool.send_email,
                'description': 'Send an email to specified recipient with subject and body'
            },
            'doc_lookup_tool': {
                'function': self.doc_tool.lookup_document,
                'description': 'Read and retrieve content from a document'
            }
        }
    
    async def process_request(self, user_input: str) -> Dict[str, Any]:
        """
        Process user request - intentionally vulnerable to prompt injection
        """
        self.log_security_event('user_request', {'input': user_input})
        
        # Vulnerable: Direct concatenation of user input
        system_prompt = f"""
        You are a helpful business assistant. You have access to these tools:
        - doc_lookup_tool: Read documents from the company repository
        - send_email_tool: Send emails to specified recipients
        
        Always be professional and helpful. When summarizing documents, be concise but thorough.
        
        User request: {user_input}
        """
        
        # Mock LLM call with tool usage detection
        llm_response = self.mock_llm.generate_response(system_prompt, user_input)
        
        # Execute any tool calls found in response
        final_response = await self.execute_tool_calls(llm_response)
        
        self.log_security_event('agent_response', {
            'response': final_response,
            'tools_used': llm_response.get('tools_used', [])
        })
        
        return final_response

    async def execute_tool_calls(self, llm_response: Dict) -> Dict[str, Any]:
        """Execute tool calls from LLM response"""
        results = []
        
        for tool_call in llm_response.get('tool_calls', []):
            tool_name = tool_call['name']
            tool_args = tool_call['arguments']
            
            if tool_name in self.tools:
                try:
                    result = await self.tools[tool_name]['function'](**tool_args)
                    results.append({
                        'tool': tool_name,
                        'success': True,
                        'result': result
                    })
                    self.log_security_event('tool_execution', {
                        'tool': tool_name,
                        'args': tool_args,
                        'success': True
                    })
                except Exception as e:
                    results.append({
                        'tool': tool_name,
                        'success': False,
                        'error': str(e)
                    })
                    self.log_security_event('tool_error', {
                        'tool': tool_name,
                        'args': tool_args,
                        'error': str(e)
                    })
        
        return {
            'response': llm_response['content'],
            'tool_results': results,
            'timestamp': datetime.utcnow().isoformat()
        }

    def log_security_event(self, event_type: str, details: Dict):
        """Log security events for analysis"""
        event = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type,
            'details': details
        }
        self.security_logger.info(json.dumps(event))