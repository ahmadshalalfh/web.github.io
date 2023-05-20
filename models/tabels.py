import datetime


db.define_table('courses',
    Field('course_code', 'string', required=True , notnull = True),
    Field('course_name', 'string' ),
    Field('description', 'text' ),
    Field('prerequisites', 'string', 'reference courses' , requires=IS_IN_DB(db,'courses.course_code','%(course_name)s')),
    Field('instructor', 'string'),


   primarykey =['course_code']
   )

db.define_table('courseschedules',
    Field('schedule_id', 'integer', required=True , notnull = True),
    Field('days', 'string'),
    Field('start_time', 'time'),
    Field('end_time', 'time', ),
    Field('room_no', 'string'),
    Field('numper_of_student','integer'),
    Field('cabasety', 'int'),
    Field('course_code', 'string','reference courses', requires=IS_IN_DB(db,'courses.course_code','%(course_name)s')),
    primarykey =['schedule_id']
   )
db.define_table('studentchedules',
    Field('schedual_id', 'integer', required=True , notnull = True),
    Field('id', 'integer', required=True , notnull = True),
    Field('days', 'string'),
    Field('start_time', 'time'),
    Field('end_time', 'time', ),
    Field('room_num', 'string'),
    Field('course_schedual','integer'),
    Field('course_code','string'),

   primarykey =['schedual_id']
   )
db.define_table('studentsregs',
    Field('id','integer'),
    Field('student_id','integer'),
    Field('course_code','string'),
    primarykey =['id']





                )

