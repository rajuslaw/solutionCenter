def get_invoice_data(invoice_id: str = None) -> str:
    return f"Invoice details for {invoice_id or 'latest'}: #12345, $250"

def get_travel_details(date: str = None) -> str:
    return f"Travel booked: NYC to LA on {date or '2024-07-02'}"
