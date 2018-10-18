{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment 1: Dino Fun World\n",
    "\n",
    "You, in your role as a burgeoning data explorer and visualizer, have been asked by the administrators of a small amusement park in your hometown to answer a couple questions about their park operations. In order to perform the requested analysis, they have provided you with a database containing information about one day of the park's operations.\n",
    "\n",
    "### Provided Database\n",
    "\n",
    "The database provided by the park administration is formatted to be readable by any SQL database library. The course staff recommends the sqlite3 library. The database contains three tables, named 'checkins', 'attractions', and 'sequences'. The information contained in each of these tables is listed below:\n",
    "\n",
    "`checkins`:\n",
    "    - Description: check-in data for all visitors for the day in the park. The data includes two types of check-ins, inferred and actual checkins.\n",
    "    - Fields: visitorID, timestamp, attraction, duration, type\n",
    "`attraction`:\n",
    "    - The attractions in the park by their corresponding AttractionID, Name, Region, Category, and type. Regions are from the VAST Challenge map such as Coaster Alley, Tundra Land, etc. Categories include Thrill rides, Kiddie Rides, etc. Type is broken into Outdoor Coaster, Other Ride, Carussel, etc.\n",
    "    - Fields: AttractionID, Name, Region, Category, type\n",
    "`sequences`:\n",
    "    - The check-in sequences of visitors. These sequences list the position of each visitor to the park every five minutes. If the visitor has not entered the part yet, the sequence has a value of 0 for that time interval. If the visitor is in the park, the sequence lists the attraction they have most recently checked in to until they check in to a new one or leave the park.\n",
    "    - Fields: visitorID, sequence\n",
    "    \n",
    "The database is named 'dinofunworld.db' and is located in the 'readonly' directory of the Jupyter Notebook environment. It can be accessed at 'readonly/dinofunworld.db'.\n",
    "\n",
    "### Questions to Answer\n",
    "\n",
    "The administrators would like you to answer four relatively simple questions about the park activities on the day in question. These questions all deal with park operations and can be answered using the data provided.\n",
    "\n",
    "Question 1: What is the most popular attraction to visit in the park?\n",
    "Question 2: What ride (note that not all attractions are rides) has the longest visit time?\n",
    "Question 3: Which Fast Food offering has the fewest visitors?\n",
    "Question 4: Compute the Skyline of number of visits and visit time for the park's ride and report the rides that appear in the Skyline.\n",
    "\n",
    "#### Administrative Notes\n",
    "\n",
    "This assignment will be graded by Coursera's grading system. In order for your answers to be correctly registered in the system, you must place the code for your answers in the cell indicated for each question. In addition, you should submit the assignment with the output of the code in the cell's display area. The display area should contain only your answer to the question with no extraneous information, or else the answer may not be picked up correctly. Each cell that is going to be graded has a set of comment lines at the beginning of the cell. These lines are extremely important and must not be modified or removed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "from datetime import timedelta\n",
    "import math\n",
    "con = sqlite3.connect('readonly/dinofunworld.db')\n",
    "cur = con.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Atmosfear\n"
     ]
    }
   ],
   "source": [
    "# Graded Cell\n",
    "# PartID:  NDnou\n",
    "# Question 1: What is the most popular attraction to visit in the park?\n",
    "# Notes: Your output should be the name of the attraction.\n",
    "cur.execute(\"SELECT attraction, COUNT(*) as c FROM checkin GROUP BY attraction ORDER BY c desc;\")\n",
    "popular_attraction_id = cur.fetchall()[0][0]\n",
    "cur.execute(\"SELECT Name FROM attraction WHERE AttractionID=\"+str(popular_attraction_id)+\";\")\n",
    "popular_attraction = cur.fetchone()[0]\n",
    "print(popular_attraction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Flight of the Swingodon\n"
     ]
    }
   ],
   "source": [
    "# Graded Cell\n",
    "# PartID: FXGHp\n",
    "# Question 2: What ride (note that not all attractions are rides) has the longest average visit time?\n",
    "# Notes: Your output should be the name of the ride.\n",
    "cur.execute(\"SELECT AttractionID, Name FROM attraction where LOWER(Category) LIKE '%ride%';\")\n",
    "attraction_name_category_list = cur.fetchall()\n",
    "ride_time_tuple = (\"\", 0)\n",
    "for (aid, name) in attraction_name_category_list:\n",
    "    cur.execute(\"SELECT duration FROM checkin where attraction=\"+str(aid)+\";\")\n",
    "    duration_list = cur.fetchall()\n",
    "    total_dur = 0\n",
    "    n = 0\n",
    "    for duration in duration_list:\n",
    "        try:\n",
    "            dur = duration[0].split(':')\n",
    "            total_dur += timedelta(int(dur[0]), int(dur[1]), int(dur[2])).total_seconds()\n",
    "            n += 1\n",
    "        except:\n",
    "            continue\n",
    "    avg_dur = total_dur / n\n",
    "    if avg_dur > ride_time_tuple[1]:\n",
    "        ride_time_tuple = (name, avg_dur)\n",
    "print(ride_time_tuple[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Theresaur Food Stop\n"
     ]
    }
   ],
   "source": [
    "# Graded Cell\n",
    "# PartID: KALua\n",
    "# Question 3: Which Fast Food offering in the park has the fewest visitors?\n",
    "# Notes: Your output should be the name of the fast food offering.\n",
    "cur.execute(\"SELECT attraction, COUNT(*) as c FROM checkin WHERE attraction IN (SELECT AttractionID FROM attraction where LOWER(type) LIKE '%fast food%') GROUP BY attraction ORDER by c asc;\")\n",
    "attraction_id = cur.fetchall()[0][0]\n",
    "cur.execute(\"SELECT Name FROM attraction where AttractionID = \" + str(attraction_id) + \";\")\n",
    "attraction_name = cur.fetchone()[0]\n",
    "print(attraction_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Wrightiraptor Mountain', 'Atmosfear', 'Dykesadactyl Thrill']\n"
     ]
    }
   ],
   "source": [
    "# Graded Cell\n",
    "# PartID: B0LUP\n",
    "# Question 4: Compute the Skyline of number of visits and visit time for the park's ride and \n",
    "#  report the rides that appear in the Skyline. \n",
    "# Notes: Remember that in this case, higher visits is better and lower visit times are better. \n",
    "#  Your output should be formatted as an array listing the names of the rides in the Skyline.\n",
    "cur.execute(\"SELECT attraction, COUNT(*) as c FROM checkin WHERE attraction IN (SELECT AttractionID FROM attraction where LOWER(Category) LIKE '%ride%') GROUP BY attraction;\")\n",
    "visit_list = cur.fetchall()\n",
    "best_visited_tuple = (0, 0)\n",
    "best_ride_time_tuple = (0, math.inf)\n",
    "best_both_tuple = (0, 0, math.inf)\n",
    "for (aid,count) in visit_list:\n",
    "    cur.execute(\"SELECT duration FROM checkin where attraction=\"+str(aid)+\";\")\n",
    "    duration_list = cur.fetchall()\n",
    "    total_dur = 0\n",
    "    n = 0\n",
    "    for duration in duration_list:\n",
    "        try:\n",
    "            dur = duration[0].split(':')\n",
    "            total_dur += timedelta(int(dur[0]), int(dur[1]), int(dur[2])).total_seconds()\n",
    "            n += 1\n",
    "        except:\n",
    "            continue\n",
    "    avg_dur = total_dur / n\n",
    "    if count > best_visited_tuple[1]:\n",
    "        best_visited_tuple = (aid, count)\n",
    "    if avg_dur < best_ride_time_tuple[1]:\n",
    "        best_ride_time_tuple = (aid, avg_dur)\n",
    "    if count > best_both_tuple[1] and avg_dur < best_both_tuple[2]:\n",
    "        best_both_tuple = (aid, count, avg_dur)\n",
    "cur.execute(\"SELECT Name FROM attraction WHERE AttractionID=\"+str(best_visited_tuple[0])+\" OR AttractionID=\"+str(best_ride_time_tuple[0])+\" OR AttractionID=\"+str(best_both_tuple[0])+\";\")\n",
    "names = cur.fetchall()\n",
    "name_list = [name[0] for name in names]\n",
    "print(name_list)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
