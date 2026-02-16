import requests

def search_jobs(role: str):
    
    # MVP MOCK DATA (zanim podłączymy API)
    
    mock_jobs = [
        {
            "title": "Senior Financial Analyst",
            "company": "Global Investment Firm",
            "description": "Looking for financial modelling, forecasting, investment analysis"
        },
        {
            "title": "Finance Manager",
            "company": "Real Estate Developer",
            "description": "Budgeting, cash flow management, financial control"
        }
    ]

    return mock_jobs
