'''
python e tuple array/list er ceye binno. **tuple first bracket diye suru korte hoy.
kintu tuple er kono element access korte hole array/list er moto third bracket diye access korte hoy.
propertyVariable=tupleName[index]
**Tuple list/array er caite onek beshi first.

**afterOne=tupleName[0:]** ekhane tuple er ek nombor element bad diye baki sob gulu print korbe.
'''
# tupleName
students = (('MSA', 'CGPA:3.43', 'NSTU'), 'Parves', 'Mahedi')
msaInfo = students[0]  # ('MSA', 'CGPA:3.43', 'NSTU')
msaCGPA = msaInfo[1]  # CGPA:3.43
print(msaCGPA)
