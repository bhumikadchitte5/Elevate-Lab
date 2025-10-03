print("🤖 Hello! I’m your College Chatbot. How can I help you today?")
print("💬 (Type 'exit' to end the chat)\n")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input in ["exit", "quit", "bye"]:
        print("🤖 Chatbot: Goodbye! Have a great day at college! 🎓")
        break

    # Greetings
    elif "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hello! Welcome to our college. How can I assist you?")
    
    # College info
    elif "college name" in user_input or "name of college" in user_input:
        print("🤖 Chatbot: Our college is ABC Institute of Technology.")
    
    # Admission
    elif "admission" in user_input:
        print("🤖 Chatbot: Admissions are open from June to August. You can apply online through the official website.")
    
    # Courses
    elif "course" in user_input or "program" in user_input:
        print("🤖 Chatbot: We offer B.Tech, M.Tech, BBA, MBA, and MCA programs.")
    
    # Fees
    elif "fee" in user_input or "fees" in user_input:
        print("🤖 Chatbot: The fee structure varies by course. Visit the 'Admissions' section on our website for details.")
    
    # Contact info
    elif "contact" in user_input or "phone" in user_input:
        print("🤖 Chatbot: You can contact us at 📞 +91-9876543210 or email 📧 info@abcit.edu")
    
    # Library
    elif "library" in user_input:
        print("🤖 Chatbot: The library is open from 9 AM to 7 PM on weekdays with a collection of 10,000+ books.")
    
    # Hostel
    elif "hostel" in user_input:
        print("🤖 Chatbot: Yes, we provide separate hostels for boys and girls with 24/7 security and Wi-Fi.")
    
    # Placement
    elif "placement" in user_input:
        print("🤖 Chatbot: Our placement cell helps students get placed in top companies like TCS, Infosys, and Wipro.")
    
    # Default
    else:
        print("🤖 Chatbot: Sorry, I didn’t understand that. Please ask about admissions, courses, fees, hostel, or placements.")
