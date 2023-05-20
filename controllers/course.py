import time
@auth.requires_login()

def copy_selected_rows(form ):

        student_id = auth.user.id


        for id in form:
            row = db.courseschedules(id)
            stu = db(db.studentchedules.id == auth.user.id).select()
            course =db(db.courses.course_code == row.course_code).select().first()

            if  course.prerequisites is  None:

                  for st in stu:
                     if st.course_code==row.course_code  :
                           redirect(URL('schedules', vars={'message': 'This course has already been registered'}))

                     elif st.days == row.days and  (st.start_time <= row.start_time <= st.end_time or st.start_time <= row.end_time <= st.end_time )   :
                                redirect(URL('schedules', vars={'message': 'The date of this course conflicts with your schedule'}))



                  if row.numper_of_student != row.cabasety:
                          db.studentchedules.insert(schedual_id=None,
                                                          course_schedual=row.schedule_id,
                                                       id=student_id,
                                                       days=row.days,
                                                       start_time = row.start_time,
                                                       end_time = row.end_time,
                                                       course_code =row.course_code,
                                                       room_num = row.room_no)


                          db(db.courseschedules.schedule_id==row.schedule_id).update(numper_of_student=row.numper_of_student + 1)
                          db.studentsregs.insert(id=None,
                                                student_id = student_id,
                                                course_code =row.course_code
                          )
                          redirect(URL('schedules', vars={'message': 'The courses you selected have been added successfully'}))
                  else:
                       redirect(URL('schedules', vars={'message': 'The number of students is sufficient'}))


            else:
              stureg = db(db.studentsregs.student_id == student_id ).select()
              for sture in stureg:

                if sture.course_code == course.prerequisites:
                    for st in stu:
                            if st.course_code==row.course_code  :
                                redirect(URL('schedules', vars={'message': 'This course has already been registered'}))



                            elif st.days == row.days and  (st.start_time <= row.start_time <= st.end_time or  st.start_time <= row.end_time <= st.end_time)  :
                                redirect(URL('schedules', vars={'message': 'The date of this course conflicts with your schedule'}))



                    if row.numper_of_student != row.cabasety:
                                 db.studentchedules.insert(schedual_id=None,
                                                          course_schedual=row.schedule_id,
                                                       id=student_id,
                                                       days=row.days,
                                                       start_time = row.start_time,
                                                       end_time = row.end_time,
                                                       course_code =row.course_code,
                                                       room_num = row.room_no)


                                 db (db.courseschedules.schedule_id==row.schedule_id).update(numper_of_student=row.numper_of_student + 1)
                                 db.studentsregs.insert(id=None,
                                                 student_id = student_id,
                                                course_code =row.course_code
                                  )
                                 redirect(URL('schedules', vars={'message': 'The courses you selected have been added successfully'}))


                    else:
                        redirect(URL('schedules', vars={'message': 'The number of students is sufficient'}))


              redirect(URL('schedules', vars={'message': 'Previous course requirements have not been registered'}))



@auth.requires_login()
def schedules():
     SESSION_TIMEOUT = 1800
     session.last_activity_time = time.time()



     grid = SQLFORM.grid(db.courseschedules , deletable=False, csv=False ,selectable=copy_selected_rows,  formargs=dict(onsubmit=copy_selected_rows),
                  selectable_submit_button=' save',editable=False )
     message = request.vars.get('message')
     response.flash=message



     if (time.time() - session.last_activity_time) > SESSION_TIMEOUT:
        auth.logout()
        redirect(URL('default', 'index'))
     else:
        session.last_activity_time = time.time()


     return dict(grid = grid)



def courses():
     SESSION_TIMEOUT = 1800
     session.last_activity_time = time.time()

     grid = SQLFORM.grid(db.courses , deletable=False, csv=False,  create=False,editable=False  )
     if (time.time() - session.last_activity_time) > SESSION_TIMEOUT:
        auth.logout()
        redirect(URL('default', 'index'))
     else:
        session.last_activity_time = time.time()
     return dict(grid = grid)


def delete(form ):

      for id in form:
         row = db.studentchedules(id)

         db( db.studentchedules.schedual_id == row.schedual_id ).delete()
         db(db.courseschedules.schedule_id==row.course_schedual ).update(numper_of_student=db.courseschedules.numper_of_student - 1)
         db( db.studentsregs.student_id==row.id and db.studentsregs.course_code ==row.course_code ).delete()





def studentschedules():
    SESSION_TIMEOUT = 1800
    session.last_activity_time = time.time()

    grid = SQLFORM.grid(db.studentchedules.id==auth.user.id ,selectable=delete,selectable_submit_button=' delete',deletable=False,  create=False,editable=False,  csv=False)
    if (time.time() - session.last_activity_time) > SESSION_TIMEOUT:
        auth.logout()
        redirect(URL('default', 'index'))
    else:
        session.last_activity_time = time.time()
    return dict(grid=grid)

def studentcourses():
    SESSION_TIMEOUT = 1800
    session.last_activity_time = time.time()

    grid = SQLFORM.grid(db.studentsregs.student_id==auth.user.id ,create=False, editable=False,csv=False,deletable=False )
    if (time.time() - session.last_activity_time) > SESSION_TIMEOUT:
        auth.logout()
        redirect(URL('default', 'index'))
    else:
        session.last_activity_time = time.time()
    return dict(grid=grid)
