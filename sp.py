import speech_recognition as sr

def get_speech_input(prompt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; check internet.")
        return ""

# Form fields
print("Fill Student Form by Voice\n")

student_name = get_speech_input("Say the Student Name:")
student_id = get_speech_input("Say the Student ID:")
department = get_speech_input("Say the Department:")

# Simulating entry
print("\n--- Entered Data ---")
print("Student Name:", student_name)
print("Student ID:", student_id)
print("Department:", department)
