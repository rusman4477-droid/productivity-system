from datetime import datetime
from db import init_db, add_activity, get_activities



def calculate_total(activities):
    total = 0
    for a in activities:
        total += a["duration"]
    return total


def show_summary(activities, total):
    if not activities:
        print("Belum ada Aktivitas")
        return
    
    print("Tanggal | Aktivitas | Durasi")
    print('-' * 35)

    for a in activities:
        print(f"{a['date']} | {a['description']} | {a['duration']} menit")

    print('-' * 35)
    print(f"Total waktu : {total} menit")


#activities = load_activities()
#total = calculate_total(activities)
#show_summary(activities, total)

def input_activity():
    while True :
        date = input("Tanggal (dd-mm-yyyy): ")
        try:
            datetime.strptime(date, '%d-%m-%Y')
            break
        except ValueError:
            print('Format tanggal salah.!!')

    description = input("Deskripsi: ")

    while True :
        duration_input = (input("Durasi (menit): "))
        if duration_input.isdigit() and int(duration_input) > 0:
            duration = int(duration_input)
            break
        else:
            print('Durasi harus angka dan lebih dari 0.')
    return date, description, duration

def summary_per_day(activities):
    summary = {}

    for a in activities:
        date = a["date"]
        duration = a["duration"]

        if date not in summary:
            summary[date] = 0
        summary[date] += duration

    return summary

def show_daily_summary(summary):
    print("Ringkasan per hari")
    print("-" * 25)

    for date in sorted(summary.keys()):
        print(f"{date} : {summary[date]} menit")

    
def summary_per_week(activities):
    summary = {}

    for a in activities:
        date_obj = datetime.strptime(a["date"], "%d-%m-%Y")
        year, week, _ = date_obj.isocalendar()
        key = f"{year}-W{week}"

        if key not in summary:
            summary[key] = 0
        summary[key] += a["duration"]

    return summary

def show_weekly_summary(summary):
    print("Ringkasan per minggu")
    print("-" * 25)

    for week in sorted(summary.keys()):
        print(f"{week} : {summary[week]} menit")


def summary_per_month(activities):
    summary = {}

    for a in activities:
        date_obj = datetime.strptime(a["date"], "%d-%m-%Y")
        key = date_obj.strftime("%m-%Y")

        if key not in summary:
            summary[key] = 0
        summary[key] += a["duration"]

    return summary

def show_monthly_summary(summary, limit = 3):
    print("\nRingkasan per bulan")
    print("-" * 30)

    months = sorted(summary.keys(), reverse=True)

    for month in months[:limit]:
        print(f"{month} : {summary[month]} menit")


def show_menu():
    print("\n=== Personal Productivity System ===")
    print("1. Tambah aktivitas")
    print("2. Lihat ringkasan")
    print("3. Keluar")
    print("4. Lihat ringkasan per hari")
    print("5. Lihat ringkasan per minggu")
    print("6. Lihat ringkasan per bulan")
init_db()

while True:
    show_menu()
    choice = input("Pilih menu: ")

    if choice == "1":
        date, description, duration = input_activity()
        add_activity(date, description, duration)
        print("Aktivitas tersimpan.")

    elif choice == "2":
        activities = get_activities()
        total = calculate_total(activities)
        show_summary(activities, total)

    elif choice == "3":
        print("Keluar. Jangan males besok lanjut.")
        break

    elif choice == "4":
        activities = get_activities()
        daily = summary_per_day(activities)
        show_daily_summary(daily)

    elif choice == "5":
        activities = get_activities()
        weekly = summary_per_week(activities)
        show_weekly_summary(weekly)

    elif choice == "6":
        activities = get_activities()
        monthly = summary_per_month(activities)
        show_monthly_summary(monthly)


    else:
        print("Pilihan ga valid.")

