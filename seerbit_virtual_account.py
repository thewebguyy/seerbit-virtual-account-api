import requests
import logging

SEERBIT_API_KEY = "SBPUBK_DQ24K6T5TI1WOAOYPWWYMGMHKDRVEGPW"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_virtual_account(public_key, full_name, bank_verification_number, currency, country, reference, email):
    url = "https://seerbitapi.com/api/v2/virtual-accounts/"
    headers = {"Authorization": f"Bearer {SEERBIT_API_KEY}"}
    data = {
        "publicKey": public_key,
        "fullName": full_name,
        "bankVerificationNumber": bank_verification_number,
        "currency": currency,
        "country": country,
        "reference": reference,
        "email": email
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to create virtual account: {e}")
        return None


def get_virtual_account(reference):
    url = f"https://seerbitapi.com/api/v2/virtual-accounts/{reference}"
    headers = {"Authorization": f"Bearer {SEERBIT_API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to get virtual account: {e}")
        return None


def update_virtual_account(reference, full_name, bank_verification_number, currency, country, email):
    url = f"https://seerbitapi.com/api/v2/virtual-accounts/{reference}"
    headers = {"Authorization": f"Bearer {SEERBIT_API_KEY}"}
    data = {
        "fullName": full_name,
        "bankVerificationNumber": bank_verification_number,
        "currency": currency,
        "country": country,
        "email": email
    }

    try:
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to update virtual account: {e}")
        return None


def delete_virtual_account(reference):
    url = f"https://seerbitapi.com/api/v2/virtual-accounts/{reference}"
    headers = {"Authorization": f"Bearer {SEERBIT_API_KEY}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {'success': True}
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to delete virtual account: {e}")
        return None


def deposit_funds(reference, amount):
    url = f"https://seerbitapi.com/api/v2/virtual-accounts/{reference}/deposit"
    headers = {"Authorization": f"Bearer {SEERBIT_API_KEY}"}
    data = {
        "amount": amount
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to deposit funds: {e}")
        return None


def withdraw_funds(reference, amount):
    url = f"https://seerbitapi.com/api/v2/virtual-accounts/{reference}/withdraw"
    headers = {"Authorization": f"Bearer {SEERBIT_API_KEY}"}
    data = {
        "amount": amount
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to withdraw funds: {e}")
        return None


def make_payment(reference, amount, recipient_account):
    url = "https://seerbitapi.com/api/v2/payments"
    headers = {"Authorization": f"Bearer {SEERBIT_API_KEY}"}
    data = {
        "reference": reference,
        "amount": amount,
        "recipientAccount": recipient_account
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to make payment: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    public_key = "SBPUBK_DQ24K6T5TI1WOAOYPWWYMGMHKDRVEGPW"
    full_name = "Jane Smith"
    bank_verification_number = ""
    currency = "NGN"
    country = "NG"
    reference = "FIRST_VIRTUAL_17"
    email = "js@emaildomain.com"

    # Create virtual account
    virtual_account = create_virtual_account(public_key, full_name, bank_verification_number, currency, country, reference, email)
    if virtual_account:
        logger.info("Virtual Account Created: %s", virtual_account)

    # Retrieve virtual account
    retrieved_account = get_virtual_account(reference)
    if retrieved_account:
        logger.info("Retrieved Virtual Account: %s", retrieved_account)

    # Update virtual account
    updated_account = update_virtual_account(reference, full_name, bank_verification_number, currency, country, email)
    if updated_account:
        logger.info("Updated Virtual Account: %s", updated_account)

    # Delete virtual account
    deletion_result = delete_virtual_account(reference)
    if deletion_result:
        logger.info("Deletion Result: %s", deletion_result)

    # Deposit funds into virtual account
    deposit_result = deposit_funds(reference, 1000)
    if deposit_result:
        logger.info("Deposit Result: %s", deposit_result)

    # Withdraw funds from virtual account
    withdrawal_result = withdraw_funds(reference, 500)
    if withdrawal_result:
        logger.info("Withdrawal Result: %s", withdrawal_result)

    # Make payment using virtual account
    recipient_account = "Recipient_Account_Number"
    payment_result = make_payment(reference, 500, recipient_account)
    if payment_result:
        logger.info("Payment Result: %s", payment_result)
