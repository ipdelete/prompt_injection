from tools.send_email_tool import send_email
from tools.doc_lookup_tool import doc_lookup

def main():
    send_email("ian", "dang it works...")
    vendor = doc_lookup("vendor_summary.pdf")
    roadmap = doc_lookup("roadmap.pdf")
    
    print(vendor)
    print(roadmap)


if __name__ == "__main__":
    main()
