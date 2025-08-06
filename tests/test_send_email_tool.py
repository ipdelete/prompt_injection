#!/usr/bin/env python

import pytest
from io import StringIO
import sys
from tools.send_email_tool import send_email


class TestSendEmailTool:
    """Test cases for the send_email function."""

    def test_send_email_basic(self, capsys):
        """Test that send_email prints the correct output for basic input."""
        send_email("test@example.com", "Test message")
        
        captured = capsys.readouterr()
        assert "Sending email to: test@example.com" in captured.out
        assert "Email body: Test message" in captured.out

    def test_send_email_empty_recipient(self, capsys):
        """Test send_email with empty recipient."""
        send_email("", "Test message")
        
        captured = capsys.readouterr()
        assert "Sending email to: " in captured.out
        assert "Email body: Test message" in captured.out

    def test_send_email_empty_body(self, capsys):
        """Test send_email with empty email body."""
        send_email("test@example.com", "")
        
        captured = capsys.readouterr()
        assert "Sending email to: test@example.com" in captured.out
        assert "Email body: " in captured.out

    def test_send_email_multiline_body(self, capsys):
        """Test send_email with multiline email body."""
        multiline_body = "Line 1\nLine 2\nLine 3"
        send_email("user@domain.com", multiline_body)
        
        captured = capsys.readouterr()
        assert "Sending email to: user@domain.com" in captured.out
        assert "Email body: Line 1\nLine 2\nLine 3" in captured.out

    def test_send_email_special_characters(self, capsys):
        """Test send_email with special characters in recipient and body."""
        send_email("user+tag@example.com", "Hello! @#$%^&*()_+")
        
        captured = capsys.readouterr()
        assert "Sending email to: user+tag@example.com" in captured.out
        assert "Email body: Hello! @#$%^&*()_+" in captured.out

    def test_send_email_unicode_content(self, capsys):
        """Test send_email with unicode characters."""
        send_email("测试@example.com", "Hello 世界! 🚀")
        
        captured = capsys.readouterr()
        assert "Sending email to: 测试@example.com" in captured.out
        assert "Email body: Hello 世界! 🚀" in captured.out

    def test_send_email_long_content(self, capsys):
        """Test send_email with long content."""
        long_recipient = "very.long.email.address.for.testing@example.com"
        long_body = "This is a very long email body. " * 50
        
        send_email(long_recipient, long_body)
        
        captured = capsys.readouterr()
        assert f"Sending email to: {long_recipient}" in captured.out
        assert f"Email body: {long_body}" in captured.out
