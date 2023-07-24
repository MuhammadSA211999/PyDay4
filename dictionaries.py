'''
python dictonaries hocce JS object er moto.
kintu python ekey hisabe number/string deya zay
dictonaries e property **key:value **pair hisebe thake.
dictionaries theke duivabe key-value access kora zay.

1. dictionaryName.keyName // key exist na korle keyError dekhabe

1. msa=tudentIds[101] //MSA

2.dictionaryName.get(keyName,'didn't found') // key exist na korle **get func er 2nd argument error hisabe trhow korbe.
zodi **get func er 2nd arguiment deya na hoy se kkhetre **none error dkbe.

2. parves = studentsIds.get(201, "Id didn't found") //Parves
studentIds er moddhye key 201 na thakle Id didn't found dekhabe.
'''
# dictName
studentsIds = {
    # key: value
    101: 'MSA',
    201: 'Parves',
    301: 'Mahedi'
}
# access dictionaries property by keyName
msa = studentsIds[101]
# print(msa) //MSA
parves = studentsIds.get(201, "Id didn't found")
# print(parves) // Parves

error = studentsIds.get(503, "Id didn't found")
# print(error) // error hisabe (Id didn't found) dekhabe
