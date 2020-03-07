from flask import render_template, flash, redirect, url_for
from app_package import app, db, mongo

from app_package.courseforms import AddCourseForm,ModifyCourseForm

course_id=0
check=True



@app.route("/add_course",methods=["GET","POST"])

def add_course():
    global course_id,check
    form=AddCourseForm()
    if form.validate_on_submit():
        fields=["_id","coursename","duration","coursefees","status","description"]
        course_col=mongo.db.courses
        if check:
                check=False
                if course_col.count()==0: 
                    course_id=0
                else:
                    cours=course_col.find().sort("_id",-1).limit(1)
                    tmp=cours.next()
                    course_id=tmp["_id"]    

        course_id+=1
        values=[course_id,form.coursename.data,form.duration.data,form.coursefees.data,form.status.data,form.description.data]
        course=dict(zip(fields,values))
        name={"coursename":form.coursename.data}
        check_name=course_col.find_one(name)
        if not bool(check_name) :
            if form.coursefees.data > 0:
                tmp=course_col.insert_one(course)
                if tmp.inserted_id==course_id:
                    flash("Course  added")
                    return redirect(url_for("display_course"))
            else:
                flash("coursefees data entered is not valid")
                return redirect(url_for("add_course"))
        else:
            flash("course that registered is existing")
            return redirect(url_for("add_course"))
    else:
        return render_template("add_course.html",form=form)

@app.route("/modify_course/<int:a>",methods=["GET","POST"])

def modify_course(a):  
    form=ModifyCourseForm()  
    course_col=mongo.db.courses
    course=course_col.find_one({"_id":a})
    if form.validate_on_submit(): 
        values=dict()
        
        if form.duration.data!="":values["duration"]=form.duration.data
        if form.coursefees.data!="" and form.coursefees.data>0:values["coursefees"]=form.coursefees.data
        else:
            flash("Invalid fee ...Cannot update")
            return redirect(url_for("display_course"))
        if form.status.data!="":values["status"]=form.status.data
        if form.description.data!="":values["description"]=form.description.data
        new_data={"$set":values}
        query={"_id":a}
        course_col=mongo.db.courses
        course_col.update_one(query,new_data)
        flash("Course modified")
        return redirect(url_for("menu"))
    else:
        return render_template("modify_course.html",form=form,course=course)

@app.route("/display_course")
def display_course():
    course_col=mongo.db.courses
    courses=course_col.find()
    return render_template("display_course.html",courses=courses)

        
       
