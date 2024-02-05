import json

f = "p1.json"

l = {
    "https://docs.google.com/spreadsheets/d/1RSGAsorx4Gln6Ba9Gdr6eyOkchNlwUvG/edit?usp=drive_link&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1AUarFwgFNZ4CRsF2pSHCXIE2QfvEJYjo/edit?usp=drive_link&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1M2EF-ZfCFAjA53XlNuHJsgLroIujjGzF/edit?usp=drive_link&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://drive.google.com/file/d/1tFSqtZUGpM4vhYhlX6ox0CIJUSWR_rKG/view?usp=drive_link",
    "https://drive.google.com/file/d/1f08V0pk2Slc7SfXvDzQCeNY55EA-h6bn/view?usp=drive_link",
    "https://drive.google.com/file/d/1dZkoAaX_cGeUStf7hZJurb9XTeOJVK3G/view?usp=drive_link",
    "https://docs.google.com/spreadsheets/d/13ukZxW4ci565aPdIkGOxv_dICuXxi8oD/edit?usp=share_link&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1jmk2G92JqmOU30XigcLhdgI5ZZn8abgL/edit?usp=drive_link&ouid=108670582734577026743&rtpof=true&sd=true",
    "Invoce: JTHTS2020-2023",
    "https://docs.google.com/spreadsheets/d/1iFlFiy_Nu3W-7KmOo1Cq_0NYfJ3jxpwf/edit?usp=share_link&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1G8TOoLp-j-s69w251k6QmypDOXSReWul/edit?usp=share_link&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/19W3SAZl56H8n_PpRTORX78KxcO05tALt/edit?usp=share_link&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1qRkJS1bjhvIUlhwekLgSHgwbSohFT8ik/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1IZci5PAt8eU59SgOg1cbNJAhkw9KpnhB/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/16TWxk_g9Es1zY6yCdbvELYTNBcWjMujN/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1bekxYhl1VT820jh1dzy_VbIYDMbtn1Pu/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1W4ZF9qOePcswMu0l3JgTQgxpXaTJYTiH/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1dp6RCgEoyP4VKdol2xMFTp9K59_-FWsA/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1gN0SEdf4d6br6hye0wLVZplQ8i0Vsk5K/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1wMzQOLZyHOLLY39bU59s7njq43SsY6N4/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1SvidmtPCOwlj7rs0Woau3iNE2tkbZyX9/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/16dwsixnj-lz_s10pUPNRvImn6jCKmKvi/edit?usp=sharing&ouid=108670582734577026743&rtpof=true&sd=true",
    "https://drive.google.com/file/d/1CKMyJEwfZ_Lv0WKSon38pP5_dnlSt4mx/view?usp=sharing",
    "https://drive.google.com/drive/folders/1FaMK8ZRXxtAqajHhf3N2Zk3IHjkXfQkY?hl=ru",
    "https://docs.google.com/spreadsheets/d/195xS304vmV-7YmkvxhE0l8XNhYRYgZqm/edit?usp=sharing&ouid=102931641912862106252&rtpof=true&sd=true",
    "https://drive.google.com/drive/folders/1FaMK8ZRXxtAqajHhf3N2Zk3IHjkXfQkY?hl=ru",
    "https://drive.google.com/file/d/1Xd9rqPMhJJ1zIJdRO852pZ87E7WSTYxT/view?usp=sharing",
    "https://docs.google.com/spreadsheets/d/1baGHJePKkztEyMvsQ2zCVji1HvGo-v31/edit#gid=1415022982",
    "https://docs.google.com/spreadsheets/d/1A2csLsE4GoVYXZWEAFTo3tjt4rOUlpwb/edit#gid=1957793100",
    "https://docs.google.com/spreadsheets/d/19Qp9aDWIMdABcmMeERv4ASk0kAfACQoj/edit#gid=204130464",
    "https://docs.google.com/spreadsheets/d/1qeTJibG4258Ce3VHBfSVO03eMzWijKwB/edit#gid=1263082050",
    "https://docs.google.com/spreadsheets/d/1OZTwh6nFkwq8VjMhmHiezBE3Ea9Miw7Q/edit#gid=1632186158",
    "https://docs.google.com/spreadsheets/d/1acS54-mcw6DudbNpDc1UvL2CjpPi4-B2/edit#gid=1841327471",
    "https://docs.google.com/spreadsheets/d/12gXampOVfb8U80iiBsbZXS5wt7gXxMeC/edit#gid=577658522",
    "https://docs.google.com/spreadsheets/d/1eRTefW2bkolLVKtwbEeF5lw9r1x5ZO5d/edit#gid=749579120",
    "https://docs.google.com/spreadsheets/d/1N7SGJ-mQSXLRALZerBWcJu8NVsFmkbzV/edit#gid=1484904197",
    "https://docs.google.com/spreadsheets/d/1xgfwgkg_NT_yQcoP9dGfUgZN4jgR1dEU/edit?usp=sharing&ouid=105988066469092692770&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1x5TjIxYr83WJ2tZ2F0C5EXmpB0sfJIot/edit#gid=2122015044",
    "https://docs.google.com/spreadsheets/d/1TyR25y4XJUJSATlbNpCAfh3IJYpaztcwLHR2PFLtvSc/edit#gid=1648827085",
    "https://docs.google.com/spreadsheets/d/1nr_ptAxBzaTzXzL9Wm115IyVDo0aQMGWhiAMuDIkYZU/edit?usp=sharing",
    "https://docs.google.com/spreadsheets/d/1JrBR3ayyg4qQvzg4TyDCOOzavzQk13Uy9nTSQVlCv6w/edit?usp=sharing",
    "https://docs.google.com/spreadsheets/d/1UgCQSxQ3dpWvmro3qIv474FODtQTG53sKeryhibgAqI/edit?usp=sharing",
    "https://docs.google.com/spreadsheets/d/1YKjnM3HD_e0uXsnq2Zy3PtoyPy1fbzXwg-TG1EpSDus/edit?usp=sharing",
    "https://docs.google.com/spreadsheets/d/1I0Xpkbm_DlbQrDrZAKWcqtceb0vfMQub/edit#gid=1114616373",
    "https://docs.google.com/spreadsheets/d/1jgfyaEJH4hzCqHXIJBcMECkksug1STMN/edit#gid=418980979",
    "https://docs.google.com/spreadsheets/d/1HbukPEBXk8J_8Xfdq5dLOM5Czc5ibJrT/edit#gid=342088259",
    "https://docs.google.com/spreadsheets/d/1ZCuJ9kjhkO0a2q_6Su4UOK5dJNv06BFOHbuL2iR6IRs/edit?usp=sharing",
    "https://docs.google.com/spreadsheets/d/17Mj6FgpGPKFxS1xb3tmK2nTO16X7ZDOGOE0r_4AZ8HE/edit?usp=sharing",
    "https://docs.google.com/spreadsheets/d/19cajldbUGyd1_q1gKWzrQrbkmgJIcAo9PTdoq0zT2Sc/edit?usp=sharing",
    "https://docs.google.com/spreadsheets/d/15TG47WRrlFMXpoiFltLiCuPCvkA-thK1bs6bGDOpIwI/edit?usp=sharing",
    "https://drive.google.com/file/d/1ajErwt_o7zLDNdVscAbrNA3uBHGRoMzS/view?usp=sharing",
    "https://drive.google.com/drive/folders/1FaMK8ZRXxtAqajHhf3N2Zk3IHjkXfQkY?hl=ru",
    "https://drive.google.com/file/d/1coEG0dbqNuS61mYvvJb8OXuc_IGnu_R1/view?usp=drive_link",
    "https://drive.google.com/drive/folders/1cn5zAqyKozN5ul4mJIpqYHixmtdaBZMl",
    "https://docs.google.com/spreadsheets/d/1AldgpB_Std7R50emQWU4fMtHWeDgINio/edit#gid=60465074",
    "https://drive.google.com/file/d/113xnvtSZsexCTYnvMGX7YvKONf89lzer/view?usp=sharing,",
    "https://docs.google.com/spreadsheets/d/1ilDOWj2gx-t4dKBLhgoZtvw-C8SYNAdc/edit?usp=drive_link&ouid=105988066469092692770&rtpof=true&sd=true",
    "https://drive.google.com/file/d/1SBEovFufvCmjX4JABEAlWtvWyOulNcxH/view?usp=sharing",
    "Bank card Industrial and Commercial Bank of China, 6222034000046332361",
    "https://drive.google.com/file/d/195RrgxUb2tf8Ec6leoGLCTi6ofCsFZVa/view?usp=sharing",
    "https://docs.google.com/spreadsheets/d/1OMU3qofUHkPK8neJpPVCKuNbnwxLSVmn/edit#gid=2002190877",
    "https://docs.google.com/spreadsheets/d/18QBxx7b2DojIy_6GYvz_b32P7F1Dx2YP/edit?usp=drive_web&ouid=105988066469092692770&rtpof=true",
    "https://docs.google.com/spreadsheets/d/1Fqff8P7Upi0_01aeZwSsCxlOIrSOf4g4/edit?usp=sharing&ouid=105988066469092692770&rtpof=true&sd=true",
    "https://docs.google.com/spreadsheets/d/1pMzQVFe6pVP9XAGXx5IK3CynpWBbjRHl/edit?usp=drive_web&ouid=105988066469092692770&rtpof=true",
    "https://docs.google.com/spreadsheets/d/150C3LgYJbUMdIoYgVFq__-396hROLFzU/edit?usp=drive_web&ouid=105988066469092692770&rtpof=true",
    "https://docs.google.com/spreadsheets/d/10VTAp4XmuTny-aNUuptMIP5Ye4NmqpEI/edit#gid=420763650"
}

with open (f, mode="r", encoding="UTF-8")as js:
    data = json.load(js)
    i = 0
    d = set()
    for el in data['data']:
        if el['description'] in l:
            i += 1
            print(el['id_label'], el['description'], sep="\t")
            l.remove(el['description']) 


    print(len(data['data']))
    print(i)
    [print(el) for el in l]
