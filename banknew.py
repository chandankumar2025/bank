import streamlit as st

# Initialize session state for accounts if not already done
if "accounts" not in st.session_state:
    st.session_state.accounts = {}  # account_number -> {"name": str, "balance": float}

# Bank operations
def create_account(name, acc_num, initial):
    if acc_num in st.session_state.accounts:
        st.error("⚠️ Account already exists!")
    else:
        st.session_state.accounts[acc_num] = {
            "name": name,
            "balance": initial
        }
        st.success(f"✅ Account created for {name} with balance ${initial}")

def deposit(acc_num, amount):
    if acc_num not in st.session_state.accounts:
        st.error("⚠️ Account not found!")
    else:
        st.session_state.accounts[acc_num]["balance"] += amount
        st.success(f"✅ Deposited ${amount}. New balance: ${st.session_state.accounts[acc_num]['balance']}")

def withdraw(acc_num, amount):
    if acc_num not in st.session_state.accounts:
        st.error("⚠️ Account not found!")
    elif st.session_state.accounts[acc_num]["balance"] < amount:
        st.error("⚠️ Insufficient funds!")
    else:
        st.session_state.accounts[acc_num]["balance"] -= amount
        st.success(f"✅ Withdrew ${amount}. New balance: ${st.session_state.accounts[acc_num]['balance']}")

def check_balance(acc_num):
    if acc_num not in st.session_state.accounts:
        st.error("⚠️ Account not found!")
    else:
        balance = st.session_state.accounts[acc_num]["balance"]
        st.info(f"💰 Account Balance: ${balance}")

def view_accounts():
    if not st.session_state.accounts:
        st.info("ℹ️ No accounts found.")
    else:
        st.subheader("All Customer Accounts")
        for acc_num, info in st.session_state.accounts.items():
            st.write(f"🔹 **{info['name']}** (Account #: `{acc_num}`) | 💵 Balance: ${info['balance']}")

def send_money(from_acc, to_acc, amount):
    if from_acc not in st.session_state.accounts:
        st.error("⚠️ Sender account not found!")
    elif to_acc not in st.session_state.accounts:
        st.error("⚠️ Receiver account not found!")
    elif st.session_state.accounts[from_acc]["balance"] < amount:
        st.error("⚠️ Insufficient funds in sender's account!")
    else:
        st.session_state.accounts[from_acc]["balance"] -= amount
        st.session_state.accounts[to_acc]["balance"] += amount
        st.success(f"✅ Sent ${amount} from `{from_acc}` to `{to_acc}`")
        st.info(f"Sender's New Balance: ${st.session_state.accounts[from_acc]['balance']}")
        st.info(f"Receiver's New Balance: ${st.session_state.accounts[to_acc]['balance']}")

# Streamlit UI
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Create Account", "Deposit", "Withdraw", "Check Balance", "View All Accounts", "Send Money"]
)

if menu == "Create Account":
    st.subheader("🆕 Create a New Account")
    name = st.text_input("Enter your name")
    acc_num = st.text_input("Enter account number")
    initial = st.number_input("Initial deposit", min_value=0.0, format="%.2f")
    if st.button("Create Account"):
        create_account(name, acc_num, initial)

elif menu == "Deposit":
    st.subheader("💰 Deposit Money")
    acc_num = st.text_input("Account number")
    amount = st.number_input("Amount to deposit", min_value=0.0, format="%.2f")
    if st.button("Deposit"):
        deposit(acc_num, amount)

elif menu == "Withdraw":
    st.subheader("🏧 Withdraw Money")
    acc_num = st.text_input("Account number")
    amount = st.number_input("Amount to withdraw", min_value=0.0, format="%.2f")
    if st.button("Withdraw"):
        withdraw(acc_num, amount)

elif menu == "Check Balance":
    st.subheader("🔎 Check Balance")
    acc_num = st.text_input("Account number")
    if st.button("Check"):
        check_balance(acc_num)

elif menu == "View All Accounts":
    st.subheader("📋 All Customer Account Details")
    view_accounts()

elif menu == "Send Money":
    st.subheader("💸 Transfer Money")
    from_acc = st.text_input("Sender's account number")
    to_acc = st.text_input("Receiver's account number")
    amount = st.number_input("Amount to send", min_value=0.0, format="%.2f")
    if st.button("Send"):
        send_money(from_acc, to_acc, amount)
