from flask import Flask , request , render_template , redirect
from models import Blog
import os
from database import session as db_session

app =  Flask(__name__)


#home page / blog showing
@app.route('/')
def home():
    all_data = db_session.query(Blog).all()
    for blog in all_data:
          blog.img = blog.img.replace("\\", "/")
          db_session.commit()
    return render_template('index.html' , data = all_data)


# add blog 
@app.route("/add_blog/" , methods = [ 'GET','POST'])
def add():
    return render_template('addBlog.html')


# adding route
@app.route('/adding_data/', methods = ['GET', 'POST'])
def adding():
    if request.method == 'POST':
        Btitle = request.form.get('btitle')
        Bdesc = request.form.get('bdesc')
        img = request.files.get('img')  # Handle file upload
        url = request.form.get('url')
        category = request.form.get('category')
        
        
        if img:
            img_path = os.path.join("static/UserImg", img.filename)
            img.save(img_path)
        
    data = Blog(img = img_path , blog_name = Btitle , blog_desc  = Bdesc , url =url , categoty= category)
    try:
            db_session.add(data)
            db_session.commit()
            return render_template("addBlog.html", success="Blog added successfully.")
    except:
         db_session.rollback()
         return render_template('addBlog.html' ,error=f"An error occurred")
     


#delete and update    
@app.route('/updateDelete/')
def pages():
    all_data = db_session.query(Blog).all()
    for blog in all_data:
          blog.img = blog.img.replace("\\", "/")
          db_session.commit()
    print(all_data)
    return render_template('updateDelete.html' , data = all_data)
    


# deleting
@app.route('/delete/<int:id>')
def delete(id):
    data = db_session.query(Blog).get(id)
    db_session.delete(data)
    db_session.commit()
    return redirect('/updateDelete/')
    
        
    
    
        

if __name__ == '__main__':
    app.run(debug=True)