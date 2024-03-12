#Author: Dakota Deets 3/12/2024
#python script designed to auto generate the required html files 
#to navigate from your movie library, to any given movie.


# import required module
import os


#Movies portion
# assign directory
directory = 'Movies'

template = open("list.html", "r")


#wipe the page
pageResult = open("listTest.html", "w")
pageResult.write("")
pageResult.close()

#ammend the logo, nav bar, and heading.
pageResult = open("listTest.html", "a")
pageResult.write(template.read(808))



#build out the table in html starting from under <h1>Movies</h1>
#fist open the table tag
pageResult.write("<table>\n")

#then read every movie's name
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file (todo: data trap non video files)
    if os.path.isfile(f):
        pageResult.write("      <tr>\n")
        pageResult.write("          <th>")
        pageResult.write(filename)
        pageResult.write("</th>\n")
        pageResult.write("      </tr>\n")

#now close the table and body tags
pageResult.write("</table>")
pageResult.write("</body>")

pageResult.close()