## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Doador

patient_ABO = input()
patient_RH = input()
donor_ABO = input()
donor_RH = input()
patient = patient_ABO + patient_RH
donor = donor_ABO + donor_RH
if (patient == "A+" and donor == "A+") or (patient == "A+" and donor == "A-") or (patient == "A+" and donor == "O+") or (patient == "A+" and donor == "O-") or (patient == "A-" and donor == "A-") or (patient == "A-" and donor == "O-"):
    print("compatível")
elif (patient == "B+" and donor == "B+") or (patient == "B+" and donor == "B-") or (patient == "B+" and donor == "O+") or (patient == "B+" and donor == "O-") or (patient == "B-" and donor == "B-") or (patient == "B-" and donor == "O-"):
    print("compatível")
elif (patient == "AB+" and donor == "AB+") or (patient == "AB+" and donor == "AB-") or (patient == "AB-" and donor == "AB-") or (patient == "AB+" and donor == "A+") or (patient == "AB+" and donor == "A-") or (patient == "AB+" and donor == "B+") or (patient == "AB+" and donor == "B-") or (patient == "AB+" and donor == "O+") or (patient == "AB+" and donor == "O-") or (patient == "AB-" and donor == "A-") or (patient == "AB-" and donor == "B-") or (patient == "AB-" and donor == "O-"):
    print("compatível")
elif (patient == "O+" and donor == "O+") or (patient == "O+" and donor == "O-") or (patient == "O-" and donor == "O-"):
    print("compatível")
else:
    print("incompatível")
