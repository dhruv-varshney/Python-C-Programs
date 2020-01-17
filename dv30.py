import pandas as pd
staff_df = pd.DataFrame([{'name':'dhruv','role':'btech'},
                         {'name':'manjul murty','role':'bds'},
                         {'name':'swarna sen','role':'se'}])
staff_df  = staff_df.set_index('name')
student_df = pd.DataFrame([{'name':'abdcd','role':'btech'},
                         {'name':'manjul murty','role':'bdm'},
                         {'name':'hghjk','role':'qwe'}])
student_df  = student_df.set_index('name')
c = pd.merge(staff_df,student_df, how = 'outer',left_index=True,right_index=True)
print(c)
