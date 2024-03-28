from openpyxl import Workbook

# একটি নতুন ইক্সেল ফাইল তৈরি করুন
wb = Workbook()

# ইক্সেল ফাইলের প্রথম শিট নিন
sheet = wb.active

# ডেটা লেখা
sheet['A1'] = 'Hello'
sheet['B1'] = 'World!'

# ইক্সেল ফাইল সেভ করুন
wb.save("example.xlsx")
