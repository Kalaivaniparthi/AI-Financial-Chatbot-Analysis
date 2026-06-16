# ==============================================
# FINANCIAL CHATBOT PROTOTYPE
# ==============================================
# This chatbot uses hardcoded data from the extracted
# financial analysis of Microsoft, Tesla, and Apple (2023-2025)
# No pandas required - runs on pure Python!
# ==============================================

# ==============================================
# HARDCODED FINANCIAL DATA (from your analysis)
# All values in millions of USD
# ==============================================

DATA = {
    "Apple": {
        2023: {
            "Total Revenue": 383285,
            "Net Income": 96995,
            "Total Assets": 352583,
            "Total Liabilities": 290437,
            "Operating Cash Flow": 110543,
            "Revenue Growth (%)": None,
            "Net Income Growth (%)": None
        },
        2024: {
            "Total Revenue": 391035,
            "Net Income": 93736,
            "Total Assets": 364980,
            "Total Liabilities": 289015,
            "Operating Cash Flow": 122151,
            "Revenue Growth (%)": 2.02,
            "Net Income Growth (%)": -3.36
        },
        2025: {
            "Total Revenue": 416161,
            "Net Income": 102932,
            "Total Assets": 372818,
            "Total Liabilities": 288994,
            "Operating Cash Flow": 104038,
            "Revenue Growth (%)": 6.42,
            "Net Income Growth (%)": 9.81
        }
    },
    "Microsoft": {
        2023: {
            "Total Revenue": 211915,
            "Net Income": 82584,
            "Total Assets": 411976,
            "Total Liabilities": 225855,
            "Operating Cash Flow": 87582,
            "Revenue Growth (%)": None,
            "Net Income Growth (%)": None
        },
        2024: {
            "Total Revenue": 245122,
            "Net Income": 88136,
            "Total Assets": 512163,
            "Total Liabilities": 277171,
            "Operating Cash Flow": 116029,
            "Revenue Growth (%)": 15.67,
            "Net Income Growth (%)": 6.72
        },
        2025: {
            "Total Revenue": 283586,
            "Net Income": 102325,
            "Total Assets": 543352,
            "Total Liabilities": 298716,
            "Operating Cash Flow": 124385,
            "Revenue Growth (%)": 15.69,
            "Net Income Growth (%)": 16.10
        }
    },
    "Tesla": {
        2023: {
            "Total Revenue": 96773,
            "Net Income": 14997,
            "Total Assets": 122920,
            "Total Liabilities": 54100,
            "Operating Cash Flow": 13656,
            "Revenue Growth (%)": None,
            "Net Income Growth (%)": None
        },
        2024: {
            "Total Revenue": 97690,
            "Net Income": 7129,
            "Total Assets": 130612,
            "Total Liabilities": 57112,
            "Operating Cash Flow": 14840,
            "Revenue Growth (%)": 0.95,
            "Net Income Growth (%)": -52.47
        },
        2025: {
            "Total Revenue": 110325,
            "Net Income": 12870,
            "Total Assets": 142800,
            "Total Liabilities": 62300,
            "Operating Cash Flow": 16500,
            "Revenue Growth (%)": 12.93,
            "Net Income Growth (%)": 80.51
        }
    }
}

COMPANIES = list(DATA.keys())
YEARS = [2023, 2024, 2025]

# ==============================================
# HELPER FUNCTIONS
# ==============================================

def format_number(num):
    """Format a number with commas for readability"""
    return f"{num:,}"

def get_company_data(company, year):
    """Get data for a specific company and year"""
    if company in DATA and year in DATA[company]:
        return DATA[company][year]
    return None

def get_latest_year_data(company):
    """Get the most recent year's data for a company"""
    if company in DATA:
        for year in sorted(DATA[company].keys(), reverse=True):
            if DATA[company][year]["Total Revenue"] is not None:
                return year, DATA[company][year]
    return None, None

# ==============================================
# CHATBOT RESPONSE FUNCTIONS
# ==============================================

def get_company_list():
    """Returns a formatted list of all companies"""
    return "Apple, Microsoft, Tesla"

def get_top_revenue_2025():
    """Finds the company with highest revenue in 2025"""
    best_company = None
    best_revenue = 0
    for company in COMPANIES:
        data = get_company_data(company, 2025)
        if data and data["Total Revenue"] > best_revenue:
            best_revenue = data["Total Revenue"]
            best_company = company
    if best_company:
        return f"{best_company} with ${format_number(best_revenue)} million"
    return "No data available"

def get_revenue_growth(company):
    """Returns revenue growth for a specific company from 2024 to 2025"""
    if company in DATA:
        growth = DATA[company][2025]["Revenue Growth (%)"]
        if growth is not None:
            return f"{company}'s revenue grew by {growth:.2f}% from 2024 to 2025."
    return f"No growth data available for {company}."

def get_net_income_growth(company):
    """Returns net income growth for a specific company from 2024 to 2025"""
    if company in DATA:
        growth = DATA[company][2025]["Net Income Growth (%)"]
        if growth is not None:
            direction = "increased" if growth > 0 else "decreased"
            return f"{company}'s net income {direction} by {abs(growth):.2f}% from 2024 to 2025."
    return f"No growth data available for {company}."

def get_company_summary(company):
    """Returns a full summary for a company"""
    if company not in DATA:
        return f"Company '{company}' not found. Available: {get_company_list()}"
    
    result = f"\n📊 {company} - Financial Summary (2023-2025):\n"
    result += "=" * 50 + "\n"
    
    for year in YEARS:
        data = get_company_data(company, year)
        if data:
            result += f"\n{year}:\n"
            result += f"  Revenue: ${format_number(data['Total Revenue'])} million\n"
            result += f"  Net Income: ${format_number(data['Net Income'])} million\n"
            result += f"  Assets: ${format_number(data['Total Assets'])} million\n"
            result += f"  Liabilities: ${format_number(data['Total Liabilities'])} million\n"
            result += f"  Operating Cash Flow: ${format_number(data['Operating Cash Flow'])} million\n"
            
            # Show growth if available
            if data["Revenue Growth (%)"] is not None:
                result += f"  Revenue Growth: {data['Revenue Growth (%)']:.2f}%\n"
            if data["Net Income Growth (%)"] is not None:
                result += f"  Net Income Growth: {data['Net Income Growth (%)']:.2f}%\n"
    
    return result

def get_general_summary():
    """Returns a high-level summary of all companies"""
    result = "\n📊 FINANCIAL SUMMARY (2025):\n"
    result += "=" * 50 + "\n"
    
    for company in COMPANIES:
        data = get_company_data(company, 2025)
        if data:
            result += f"\n{company}:\n"
            result += f"  Revenue: ${format_number(data['Total Revenue'])} million\n"
            result += f"  Net Income: ${format_number(data['Net Income'])} million\n"
            if data["Revenue Growth (%)"] is not None:
                result += f"  Revenue Growth: {data['Revenue Growth (%)']:.2f}%\n"
    
    return result

def get_cash_flow_summary():
    """Returns cash flow data for all companies"""
    result = "\n💵 OPERATING CASH FLOW (2025):\n"
    result += "=" * 50 + "\n"
    
    for company in COMPANIES:
        data = get_company_data(company, 2025)
        if data:
            result += f"\n{company}: ${format_number(data['Operating Cash Flow'])} million\n"
    
    return result

def get_help():
    """Returns the list of available commands"""
    return """
I can answer these questions:
  1. "What companies are available?" or "companies"
  2. "Which company has the highest revenue in 2025?" or "highest revenue"
  3. "How has [Company]'s revenue changed?" (e.g., "How has Apple's revenue changed?")
  4. "How has [Company]'s net income changed?" (e.g., "How has Tesla's net income changed?")
  5. "Show summary for [Company]" (e.g., "Show summary for Microsoft")
  6. "Show general summary" or "summary"
  7. "Show cash flow summary" or "cash flow"
  8. "help" to show this list
  9. "exit" or "quit" to end the chat
"""

# ==============================================
# MAIN CHATBOT ENGINE
# ==============================================

def chatbot(user_query):
    """Main chatbot function - responds to user queries"""
    query = user_query.lower().strip()
    
    # ==========================================
    # PREDEFINED QUERIES
    # ==========================================
    
    # Greeting
    if query in ["hello", "hi", "hey"]:
        return "Hello! I'm your Financial Assistant. I can answer questions about Microsoft, Tesla, and Apple's financial performance from 2023 to 2025. Type 'help' to see what I can do!"
    
    # Help
    if query in ["help", "what can you do?", "commands"]:
        return get_help()
    
    # Companies list
    if query in ["what companies are available?", "companies", "list companies"]:
        return f"The companies in my database are: {get_company_list()}"
    
    # Highest revenue 2025
    if query in ["which company has the highest revenue in 2025?", "top revenue 2025", "highest revenue"]:
        return f"The company with the highest revenue in 2025 is {get_top_revenue_2025()}."
    
    # Revenue growth by company
    if "revenue" in query and ("growth" in query or "changed" in query):
        for company in COMPANIES:
            if company.lower() in query:
                return get_revenue_growth(company)
        return "Please specify a company: Apple, Microsoft, or Tesla. Example: 'How has Apple's revenue changed?'"
    
    # Net income growth by company
    if "net income" in query and ("growth" in query or "changed" in query):
        for company in COMPANIES:
            if company.lower() in query:
                return get_net_income_growth(company)
        return "Please specify a company: Apple, Microsoft, or Tesla. Example: 'How has Tesla's net income changed?'"
    
    # Summary for specific company
    if "summary for" in query or "show summary for" in query:
        for company in COMPANIES:
            if company.lower() in query:
                return get_company_summary(company)
    
    # General summary
    if query in ["show general summary", "general summary", "summary", "overview"]:
        return get_general_summary()
    
    # Cash flow summary
    if query in ["show cash flow summary", "cash flow", "operating cash flow"]:
        return get_cash_flow_summary()
    
    # Direct company name - show data
    for company in COMPANIES:
        if company.lower() in query and len(query.split()) <= 3:
            return get_company_summary(company)
    
    # Exit
    if query in ["exit", "quit", "bye", "goodbye"]:
        return "Goodbye! Have a great day!"
    
    # Default response
    return """
I don't understand that query. Here are the questions I can answer:
  1. "What companies are available?"
  2. "Which company has the highest revenue in 2025?"
  3. "How has [Company]'s revenue changed?" (e.g., "How has Apple's revenue changed?")
  4. "How has [Company]'s net income changed?" (e.g., "How has Tesla's net income changed?")
  5. "Show summary for [Company]"
  6. "Show general summary"
  7. "Show cash flow summary"
  8. "help"
  9. "exit" or "quit"
"""

# ==============================================
# RUN THE CHATBOT
# ==============================================

if __name__ == "__main__":
    print("=" * 60)
    print("🤖 FINANCIAL CHATBOT PROTOTYPE")
    print("=" * 60)
    print("\nHello! I'm your Financial Assistant.")
    print("I can answer questions about Microsoft, Tesla, and Apple (2023-2025).")
    print("\nType 'help' to see all available commands.")
    print("Type 'exit' or 'quit' to end the chat.")
    print("\n" + "-" * 60)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                print("Bot: Goodbye! Have a great day!")
                break
            
            response = chatbot(user_input)
            print(f"Bot: {response}")
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\nBot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"Bot: Sorry, an error occurred: {e}")
