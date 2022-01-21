import face_recognition
import cv2
import numpy as np
import os
import glob
import csv
from datetime import date





def main():
    faces_encodings = []
    faces_names = []

    global cur_direc
    cur_direc = os.getcwd()

    path = os.path.join(cur_direc, 'data/faces/')

    list_of_files = [f for f in glob.glob(path+'*.jpg')]

    number_files = len(list_of_files)

    names = list_of_files.copy()



    #train the faces
    for i in range(number_files):
        globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])

        try:
            
            globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]

        except IndexError as e:
            print("No face is found for {}".format(list_of_files[i]))
            pass
            

        faces_encodings.append(globals()['image_encoding_{}'.format(i)])
        #create an array of known names
        names[i] = names[i].replace(cur_direc, "")
        faces_names.append(names[i])



    #face recognition

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    print_name = []
    global print_names
    print_names = []
    absen = []
    global absent
    absent = []
    global datee
    datee = date.today()


    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(faces_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(faces_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = faces_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

    #display the result
        for(top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            #draw a rectangle aroutn the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            print_name.append(name)
            

        #display the resulting image
        cv2.imshow('Video', frame)

        #hit 'q' on the keyboard to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            for i in faces_names:
                if i not in print_name:
                    absen.append(i)

            for x in absen:
                y = x.replace('\\data/faces\\', '')
                z = y.replace('.jpg', '')
                w = "HCS/" + z
                absent.append(w)
            
            print_name = list(dict.fromkeys(print_name))
            for x in print_name:
                y = x.replace('\\data/faces\\', '')
                z = y.replace('.jpg', '')
                w = "HCS/" + z
                print_names.append(w)
            break



    video_capture.release()
    cv2.destroyAllWindows()


def ccsv(others):
    with open (cur_direc + '/Attendance' + str(datee) + '.csv', 'w', newline = '') as csvfile:
                my_writer = csv.writer(csvfile, delimiter = ' ')
                my_writer.writerow(others)
                my_writer.writerow('Present')
                my_writer.writerows(print_names)
                my_writer.writerow('Absent')
                my_writer.writerows(absent)
                
                





            














