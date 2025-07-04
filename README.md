# Business Contact List Cleaner

  A Python tool to clean and standardize business contact databases.

  ## Features
  - ✅ Remove duplicate contacts by email
  - ✅ Standardize phone number formats
  - ✅ Validate email addresses
  - ✅ Export clean CSV file
  - ✅ Detailed processing summary

  ## Usage
  ```bash
  # Activate virtual environment
  source contact_cleaner_env/bin/activate

  # Run the cleaner
  python3 contact_cleaner.py

  Input Format

  CSV file with columns: name, email, phone, company

  Output

  - cleaned_contacts.csv - Processed data
  - Processing summary with statistics
  - Email validation results
  - Phone number standardization

  Example Results

  📈 Original contacts: 51
  🔄 After deduplication: 49
  ❌ Duplicates removed: 2
  ✉️ Valid emails: 44
  ⚠️ Invalid emails: 5

  Perfect for sales teams, marketing databases, and CRM cleanup.

  Technologies

  - Python 3
  - Pandas for data processing
  - Regex for validation
  - CSV processing