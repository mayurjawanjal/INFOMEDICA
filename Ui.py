from tkinter import *
import pandas as pd
import diseasePrediction
import tkentrycomplete


def diseasePredict():
    window = Tk()
    window.title("Disease Prediction..")
    df=pd.read_csv("Dataset/dis_sym_dataset_norm.csv")

    X=df.iloc[:, 1:]
    dis_symptoms = list(X.columns)

    Symptom1 = StringVar()
    Symptom1.set("")
    Symptom2 = StringVar()
    Symptom2.set("")
    Symptom3 = StringVar()
    Symptom3.set("")
    Symptom4 = StringVar()
    Symptom4.set("")
    Symptom5 = StringVar()
    Symptom5.set("")

    def predict():
        symptoms=[Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
        final_symptoms = [i for i in symptoms if i]
        t1.delete("1.0",END)
        t1.insert(END,diseasePrediction.predictDisease(final_symptoms))

    S1Lb = Label(window, text="Symptom 1")
    S1Lb.grid(row=7, column=0, pady=10, sticky=W)

    S2Lb = Label(window, text="Symptom 2")
    S2Lb.grid(row=8, column=0, pady=10, sticky=W)

    S3Lb = Label(window, text="Symptom 3")
    S3Lb.grid(row=9, column=0, pady=10, sticky=W)

    S4Lb = Label(window, text="Symptom 4")
    S4Lb.grid(row=10, column=0, pady=10, sticky=W)

    S5Lb = Label(window, text="Symptom 5")
    S5Lb.grid(row=11, column=0, pady=10, sticky=W)

    lrLb = Label(window, text="According to me disease may be")
    lrLb.grid(row=15, column=0, pady=10,sticky=W)


    symptom1_combo = tkentrycomplete.AutocompleteCombobox(textvariable=Symptom1)
    symptom2_combo = tkentrycomplete.AutocompleteCombobox(textvariable=Symptom2)
    symptom3_combo = tkentrycomplete.AutocompleteCombobox(textvariable=Symptom3)
    symptom4_combo = tkentrycomplete.AutocompleteCombobox(textvariable=Symptom4)
    symptom5_combo = tkentrycomplete.AutocompleteCombobox(textvariable=Symptom5)


    symptom1_combo.set_completion_list(dis_symptoms)
    symptom2_combo.set_completion_list(dis_symptoms)
    symptom3_combo.set_completion_list(dis_symptoms)
    symptom4_combo.set_completion_list(dis_symptoms)
    symptom5_combo.set_completion_list(dis_symptoms)


    symptom1_combo.grid(row=7, column = 1)
    symptom2_combo.grid(row=8, column = 1)
    symptom3_combo.grid(row=9, column = 1)
    symptom4_combo.grid(row=10, column = 1)
    symptom5_combo.grid(row=11, column = 1)


    t1 = Text(window, height=1, width=40,bg="orange",fg="black")
    t1.grid(row=15, column=1, padx=10)

    dst = Button(window, text="predict", command=predict)
    dst.grid(row=15, column=3,padx=10)
    window.mainloop() 
