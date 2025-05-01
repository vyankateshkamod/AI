# Elementary Chatbot with Enhanced Options

# Algorithm:
# 1. Display a list of fixed user options (menu-driven).
# 2. Based on input, respond with appropriate message.
# 3. Ask for additional input only when necessary.
# 4. Repeat until the user selects 'Exit'.

def display_menu():
    print("\n📋 How can I assist you today?")
    print("1. Track my order")
    print("2. Cancel my order")
    print("3. Return/Exchange product")
    print("4. Help / FAQs")
    print("5. Submit feedback")
    print("6. Say Hello")
    print("7. Exit")

def chatbot():
    print("👋 Welcome to ShopEasy Chatbot!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            order_id = input("Please enter your Order ID to track: ")
            print(f"🔎 Your order {order_id} is on its way and will be delivered soon!")

        elif choice == '2':
            order_id = input("Enter the Order ID to cancel: ")
            print(f"❌ Your order {order_id} has been cancelled successfully.")

        elif choice == '3':
            order_id = input("Enter Order ID for return/exchange: ")
            reason = input("Reason for return/exchange: ")
            print(f"🔁 Your request for Order {order_id} has been recorded with reason: {reason}. We’ll contact you soon.")

        elif choice == '4':
            print("\n📖 Frequently Asked Questions:")
            print("- Q: How to track my order?\n  A: Choose option 1 and enter your Order ID.")
            print("- Q: Can I cancel a delivered order?\n  A: No, only orders that are not delivered yet can be cancelled.")
            print("- Q: How do I return a product?\n  A: Use option 3 and provide the reason.")

        elif choice == '5':
            feedback = input("We value your feedback. Please enter it below:\n")
            print("🙏 Thank you for your valuable feedback!")

        elif choice == '6':
            print("😊 Hello there! I'm here to assist you with your shopping experience.")

        elif choice == '7':
            print("👋 Thank you for using ShopEasy Chatbot. Have a great day!")
            break

        else:
            print("⚠️ Invalid input. Please choose a valid option from 1 to 7.")

# Run the chatbot
chatbot()
