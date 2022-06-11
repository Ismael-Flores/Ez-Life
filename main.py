from website import create_app

app = create_app()

#Only if we run this file,we will execute the following line app.run(debug=TRUE)
if __name__ == '__main__':
    app.run(debug=True)
