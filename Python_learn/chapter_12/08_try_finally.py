try:
    f = open("sample.txt", "w")
    f.write("Hello Shiv 🌸")
    print("✅ File written successfully!")
except Exception as e:
    print("❌ Error occurred:", e)
finally:
    f.close()
    print("📂 File closed safely (finally block always runs).")
