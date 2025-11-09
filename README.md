Student performance flow
1- library for gissing the gender ( see what to do with m issing names in this step mostly ignore that row first check # of rows that miss both gender and name -> only one, drop or maybe mode?)
2- ignore first two columns (identifiers)
733/1000 columns remanin after these two steps but I don't want to remove the others so I'll handle missing values by different ways as mentioned below
3- AttendanceRate	StudyHoursPerWeek	PreviousGrade FinalGrade	Study Hours	Attendance (%) (mean) [how does this work exactly? like does all the missing values get the same value?]
4- ExtracurricularActivities	ParentalSupport Online Classes Taken (Mode)
5- how does the impute function perform?
Handling redunduncy
1- assumed the week is 5 days 
2- calculated the studyhours perday from the StudyHoursPerWeek. 
3- calculated the study hours per week from study hours. 
4- created two new columns based on the same idea one have the average of the essential studyhours perday and the one I calculated, 
the other is the average essential study hours per week and the one I calculated. 
now I'm going to depend on only one of the new two columns and drop the others. does this make anysense or just هبد؟ I want a scientific reasonable answer.
----> Now the new two coulumns correspond to the same #of horus
Dealing with negative values
there's many approaches 
1- remove
2- impute 
3- directly conert to positive, sine they're only 6 values that won't effect I'll stick to directly convert them to positive.
