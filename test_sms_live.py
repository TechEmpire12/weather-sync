
import sys
import argparse
from sms_service import SMSService

def main():
    """
    CLI tool to send a test SMS using the project's SMSService.
    Usage: python test_sms_live.py <PHONE_NUMBER> [MESSAGE]
    """
    parser = argparse.ArgumentParser(description="Test Termii SMS Integration")
    parser.add_argument("phone", help="Recipient phone number (e.g., 2348012345678)")
    parser.add_argument("message", nargs="?", default="This is a test message from your Agro-Weather System.", help="Message content")
    parser.add_argument("--sender", help="Override the Sender ID (default: from .env)", default=None)
    
    args = parser.parse_args()
    
    print(f"Initializing SMS Service...")
    sms = SMSService()
    
    if args.sender:
        print(f"Overriding Sender ID to: {args.sender}")
        sms.sender_id = args.sender
    
    if not sms.is_configured():
        print("Error: SMS Service is not configured. Check your TERMII_API_KEY in .env")
        sys.exit(1)
        
    print(f"Sending to: {args.phone}")
    print(f"Message: {args.message}")
    print("-" * 30)
    
    result = sms.send_alert(args.phone, args.message)
    
    print("Response from Termii:")
    print(result)
    
    if result.get("success"):
        print("\n✅ SMS Sent Successfully!")
    else:
        print("\n❌ SMS Failed.")

if __name__ == "__main__":
    main()
