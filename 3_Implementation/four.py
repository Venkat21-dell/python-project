txtDisplay = Entry(calc,
                   font=('Helvetica', 20,
                         'bold'),
                   bg='black',
                   fg='white',
                   bd=30,
                   width=28,
                   justify=RIGHT)
 
txtDisplay.grid(row=0,
                column=0,
                columnspan=4,
                pady=1)
 
txtDisplay.insert(0, "0")