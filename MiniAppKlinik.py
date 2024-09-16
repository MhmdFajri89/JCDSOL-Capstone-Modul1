from tabulate import tabulate
from datetime import datetime
import re

strEqual = "=" * 10
patientRegistred = [
    {
        "RegistrationNo": "A001",
        "PatientName": "Rusnelly",
        "Age": 38,
        "Gender": "Laki-laki",
        "Room": "Poli Kulit",
        "Physician": "dr. Tudung, SpKK",
        "Guarantor": "Pribadi",
        "RegistrationDate": "15-09-2024",
        "Soap": {
            "Subjective": "hidung bengkak",
            "Objective": "sakit ringan",
            "Assessment": "B02 Zoster [herpes zoster]",
            "Planning": ""
        }
    },
    {
        "RegistrationNo": "A002",
        "PatientName": "Ridon Permadi",
        "Age": 36,
        "Gender": "Laki-laki",
        "Room": "Poli Umum",
        "Physician": "dr. Ardiman",
        "Guarantor": "Pribadi",
        "RegistrationDate": "15-09-2024",
        "Soap": {
            "Subjective": "nyeri di kedua lutut kaki",
            "Objective": "Kesadaran: Composmentis, GCS: E: 4 M: 6 V: 5",
            "Assessment": "M25.56 M25.56 - Pain in joint, lower leg",
            "Planning": ""
        }
    },
    {
        "RegistrationNo": "A003",
        "PatientName": "Bisara Sitorus",
        "Age": 43,
        "Gender": "Laki-laki",
        "Room": "Poli Paru",
        "Physician": "dr. Efendy, SpP",
        "Guarantor": "BPJS",
        "RegistrationDate": "15-09-2024",
        "Soap": {
            "Subjective": "batuk sesak napas",
            "Objective": "Kesadaran: Composmentis, GCS: E: 4 M: 6 V: 5",
            "Assessment": "J47 J47 - Bronchiectasis",
            "Planning": "terapi teruskan"
        }
    },
    {
        "RegistrationNo": "A004",
        "PatientName": "Yeni Hariyani",
        "Age": 36,
        "Gender": "Perempuan",
        "Room": "Poli OBSGYN",
        "Physician": "dr. Sindhung, Sp.OG",
        "Guarantor": "Pribadi",
        "RegistrationDate": "15-09-2024",
        "Soap": {
            "Subjective": "Rujukan dgn noninflamasi",
            "Objective": "USG : Uterus RF 7,0 X 5,2 X 4,8 Cm",
            "Assessment": "N76 Other inflammation of vagina",
            "Planning": "Saran KB Karet"
        }
    }
]

def FormatSoap(soap):
    return "\n".join([f"{key}: {value}" for key, value in soap.items()])

def InvalidOption():
    print("Pilihan tidak valid! Silakan coba lagi.")

def SubMenuCaption(title, option1):
    print(f"\n{strEqual} {title} Data Pasien {strEqual}\n")
    print(f"1. {option1} Data Pasien")
    print("2. Kembali Ke Menu Utama")

def LoadByRegistrationNo(regNo):
    return next((patient for patient in patientRegistred if patient["RegistrationNo"] == regNo), None)


## Read Section
def PatientDataTable(dataTable):
    patients = []
    for pat in dataTable:
        soapStr = FormatSoap(pat["Soap"])
        patients.append([
            pat["RegistrationNo"],
            pat["PatientName"],
            pat["Age"],
            pat["Gender"],
            pat["Room"],
            pat["Physician"],
            pat["Guarantor"],
            pat["RegistrationDate"],
            soapStr
        ])
    headers = ["Reg No", "Patient Name", "Age", "Gender", "Room", "Physician", "Guarantor", "Date", "Soap"]
    print(tabulate(patients, headers=headers, tablefmt="grid"))

def ReadDataPatient():
    while True:
        print(f"\n{strEqual} Report Data Pasien {strEqual}\n")
        print("1. Report Seluruh Data")
        print("2. Report Data Tertentu")
        print("3. Kembali Ke Menu Utama")
        
        option = input("Pilih opsi (1-3): ")
        
        if option == "1":
            print("\nDaftar Pasien Registrasi:")
            PatientDataTable(patientRegistred)
        elif option == "2":
            regNo = input("Masukkan Nomor Registrasi: ").upper()
            patient = LoadByRegistrationNo(regNo)
            
            if patient:
                print(f"\nData Pasien Registrasi {regNo}:")
                PatientDataTable([patient])
            else:
                print(f"Data dengan RegistrationNo {regNo} tidak ditemukan.")
        elif option == "3":
            break
        else:
            InvalidOption()
## End Read Section


## Create Section
def CreateNewPatient():
    while True:
        SubMenuCaption("Menambahkan", "Tambah")
        option = input("Pilih opsi (1-2): ")
        
        if option == "1":
            while True:
                regNo = input("Masukkan Registration No (contoh: A001): ").upper()
                if not re.match(r"^[A-Za-z]\d{3}$", regNo):
                    print("Nomor Registrasi tidak valid! Harus berupa format Alfabet + 3 Digit Angka (contoh: A001).")
                    continue

                if LoadByRegistrationNo(regNo):
                    print(f"Data dengan nomor registrasi {regNo} sudah ada. Tidak bisa memasukkan data yang sama.")
                else:
                    break

            newPatient = {
                "RegistrationNo": regNo,
                "PatientName": input("Masukkan Nama Pasien: "),
                "Age": input("Masukkan Umur: "),
                "Gender": input("Masukkan Jenis Kelamin: "),
                "Room": input("Masukkan Ruangan: "),
                "Physician": input("Masukkan Dokter: "),
                "Guarantor": input("Masukkan Penjamin: "),
                "RegistrationDate": datetime.now().strftime("%d-%m-%Y"),
                "Soap": {
                    "Subjective": input("Masukkan SOAP - Subjective: "),
                    "Objective": input("Masukkan SOAP - Objective: "),
                    "Assessment": input("Masukkan SOAP - Assessment: "),
                    "Planning": input("Masukkan SOAP - Planning: ")
                },
            }

            while True:
                confirm = input("\nSimpan data ini? (Y/N): ").lower()
                if confirm == "y":
                    patientRegistred.append(newPatient)
                    print("Data telah disimpan.")
                    break
                elif confirm == "n":
                    print("Data tidak disimpan.")
                    break
                else:
                    InvalidOption()
        elif option == "2":
            break
        else:
            InvalidOption()
## End Create Section


## Update Section
def UpdateDataPatient():
    while True:
        SubMenuCaption("Mengubah", "Ubah")
        option = input("Pilih opsi (1-2): ")
        
        if option == "1":
            regNo = input("Masukkan Registration No: ")
            patient = LoadByRegistrationNo(regNo)

            if patient:
                PatientDataTable([patient])

                while True:
                    confirmContinueUpdate = input("\nApakah anda ingin melanjutkan Update data? (Y/N): ").lower()
                    if confirmContinueUpdate == "y":
                        validFields = {
                            "patientname": "PatientName",
                            "name": "PatientName",
                            "age": "Age",
                            "gender": "Gender",
                            "room": "Room",
                            "physician": "Physician",
                            "guarantor": "Guarantor",
                            "subjective": "Soap.Subjective",
                            "objective": "Soap.Objective",
                            "assessment": "Soap.Assessment",
                            "planning": "Soap.Planning"
                        }

                        while True:
                            fieldUpdateInput = input("Masukkan kolom yang ingin di edit: ").lower().replace(" ","")
                            
                            if fieldUpdateInput in validFields:
                                UpdateInput = input(f"Masukkan perubahan untuk {validFields[fieldUpdateInput]}: ")

                                while True:
                                    confirmUpdate = input("\nApakah data akan diupdate? (Y/N): ").lower()
                                    if confirmUpdate == "y":
                                        fieldToUpdate = validFields[fieldUpdateInput]
                                        if "Soap" in fieldToUpdate:
                                            soapField = fieldToUpdate.split(".")[1]
                                            patient["Soap"][soapField] = UpdateInput
                                        else:
                                            patient[fieldToUpdate] = UpdateInput

                                        print("Data telah terupdate.")
                                        break
                                    elif confirmUpdate == "n":
                                        print("Data batal diupdate.")
                                        break
                                    else:
                                        InvalidOption()
                                break
                            else:
                                print(f"Kolom '{fieldUpdateInput}' tidak valid. Coba lagi.")
                        break
                    elif confirmContinueUpdate == "n":
                        print("Data batal diupdate.")
                        break
                    else: 
                        InvalidOption()
            else:
                print("Data yang anda masukkan tidak ada!")
                continue
        elif option == "2":
            break
        else:
            InvalidOption()
## End Update Section


## Delete Section
def DeleteDataPatient():
    while True:
        SubMenuCaption("Menghapus", "Hapus")
        option = input("Pilih opsi (1-2): ")
        
        if option == "1":
            regNo = input("Masukkan Registration No: ")

            if LoadByRegistrationNo(regNo):
                while True:
                    confirmContinueUpdate = input("\nApakah data akan dihapus? (Y/N): ").lower()
                    if confirmContinueUpdate == "y":
                        global patientRegistred
                        patientRegistred = [patient for patient in patientRegistred if patient["RegistrationNo"] != regNo.upper()]
                        print(f"Data dengan RegistrationNo {regNo} telah dihapus.")
                        break
                    elif confirmContinueUpdate == "n":
                        print(f"Data dengan RegistrationNo {regNo} tidak jadi dihapus.")
                        break
                    else:
                        InvalidOption()

            else:
                print(f"Data yang anda masukkan tidak ada!")
                continue
        elif option == "2":
            break
        else:
            InvalidOption()
## End Delete Section


## Exit
def ExitMenu():
    print("Terima kasih.")
    exit()

## Main Menu Section
def MainMenu():
    menuOptions = {
        "1": ReadDataPatient,
        "2": CreateNewPatient,
        "3": UpdateDataPatient,
        "4": DeleteDataPatient,
        "5": ExitMenu
    }
    
    while True:
        print("=" * 15, "Data Record Pasien Klinik Sehat Bersama", "=" * 15, "\n")
        print("1. Report Data Pasien")
        print("2. Menambahkan Pasien Baru")
        print("3. Mengubah Data Pasien")
        print("4. Menghapus Data Pasien")
        print("5. Keluar")

        mainMenuInputOption = input("Silahkan Pilih Menu (1-5) : ")

        if mainMenuInputOption in menuOptions:
            menuOptions[mainMenuInputOption]()
        else:
            InvalidOption()               
        
MainMenu()
## End Main Menu Section