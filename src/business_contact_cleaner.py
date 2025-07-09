import pandas as pd
import re

def clean_contact_list(input_file):
    """
    Clean business contact list:
    - Remove duplicates by email
    - Format phone numbers
    - Validate emails
    - Generate summary report
    """
    print("🔄 Loading contact data...")

    # Load data
    df = pd.read_csv(input_file)
    original_count = len(df)

    print(f"📊 Original contacts: {original_count}")

    # Remove duplicates by email
    df_clean = df.drop_duplicates(subset=['email'], keep='first').copy()
    after_dedup = len(df_clean)

    # Clean phone numbers (keep only numbers and +)
    if 'phone' in df_clean.columns:
        df_clean.loc[:, 'phone_cleaned'] = df_clean['phone'].str.replace(r'[^\d+]', '', regex=True)

    # Validate emails
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    df_clean.loc[:, 'email_valid'] = df_clean['email'].str.match(email_pattern, na=False)

    valid_emails = df_clean['email_valid'].sum()
    invalid_emails = len(df_clean) - valid_emails

    # Save results
    output_file = 'cleaned_contacts.csv'
    df_clean.to_csv(output_file, index=False)

    # Results report
    print("\n" + "="*50)
    print("✅ CLEANING COMPLETE!")
    print("="*50)
    print(f"📈 Original contacts: {original_count}")
    print(f"🔄 After deduplication: {after_dedup}")
    print(f"❌ Duplicates removed: {original_count - after_dedup}")
    print(f"✉️  Valid emails: {valid_emails}")
    print(f"⚠️  Invalid emails: {invalid_emails}")
    print(f"💾 Clean file saved: {output_file}")
    print("="*50)

    return df_clean

def main():
    """Main function to run the cleaner"""
    input_file = '../data/demo_contacts.csv'

    try:
        result = clean_contact_list(input_file)
        print(f"\n🎉 Success! Cleaned {len(result)} contacts ready for use.")

    except FileNotFoundError:
        print(f"❌ Error: {input_file} not found!")
        print("💡 Make sure you have a CSV file with columns: name, email, phone, company")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
