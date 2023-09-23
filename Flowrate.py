import cv2
import matplotlib.pyplot as plt
import numpy as np



# Function to handle mouse click events






class flowrate:
        def __init__(self, file):
                self.file = file
                self.video = cv2.VideoCapture(r"{}".format(self.file))


        def setx1(self):

                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                frame_processed, frame = video.read()
                # Check if the frame was read successfully
                if frame_processed:
                        # Create a figure and axis for the image
                        fig, ax = plt.subplots()

                        # Display the image using Matplotlib
                        ax.imshow(frame)

                        # Define the horizontal line parameters (e.g., y-coordinate and color)
                        y_coordinate = (min(plt.ylim()) + max(plt.ylim())) / 2  # Adjust this value to set the y-coordinate of the horizontal line
                        line_color = 'red'  # Adjust this value to set the color of the line

                        # Plot the horizontal line on top of the image
                        ax.axhline(y=y_coordinate, color=line_color, linestyle='--', linewidth=2)
                        points = plt.ginput(n=1, show_clicks=True, mouse_add=1, mouse_pop=3)
                        self.x1 = int(points[0][0])
                        plt.close()

                else:
                        print("did not process")



        def setx2(self):

                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                frame_processed, frame = video.read()
                # Check if the frame was read successfully
                if frame_processed:
                        # Create a figure and axis for the image
                        fig, ax = plt.subplots()

                        # Display the image using Matplotlib
                        ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                        # Define the horizontal line parameters (e.g., y-coordinate and color)
                        y_coordinate = (min(plt.ylim()) + max(plt.ylim())) / 2  # Adjust this value to set the y-coordinate of the horizontal line
                        line_color = 'blue'  # Adjust this value to set the color of the line

                        # Plot the horizontal line on top of the image
                        ax.axhline(y=y_coordinate, color=line_color, linestyle='--', linewidth=2)
                        points = plt.ginput(n=1, show_clicks=True, mouse_add=1, mouse_pop=3)
                        self.x2 = int(points[0][0])
                        plt.close()

                else:
                        print("did not process")

        def setThreshold(self, threshold):
                self.threshold = threshold

        def sety(self):

                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                frame_processed, frame = video.read()
                # Check if the frame was read successfully
                if frame_processed:
                        # Create a figure and axis for the image
                        fig, ax = plt.subplots()

                        # Display the image using Matplotlib
                        ax.imshow(frame)

                        # Define the horizontal line parameters (e.g., y-coordinate and color)
                        x_coordinate = (min(plt.xlim()) + max(plt.xlim())) / 2  # Adjust this value to set the y-coordinate of the horizontal line
                        line_color = 'red'  # Adjust this value to set the color of the line

                        # Plot the horizontal line on top of the image
                        ax.axvline(x=x_coordinate, color=line_color, linestyle='--', linewidth=2)
                        points = plt.ginput(n=1, show_clicks=True, mouse_add=1, mouse_pop=3)
                        self.y = int(points[0][1])
                        plt.close()

                else:
                        print("did not process")


        def setHeight(self):

                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                frame_processed, frame = video.read()
                # Check if the frame was read successfully
                if frame_processed:
                        # Create a figure and axis for the image
                        fig, ax = plt.subplots()

                        # Display the image using Matplotlib
                        ax.imshow(frame)

                        # Define the horizontal line parameters (e.g., y-coordinate and color)
                        x_coordinate = (min(plt.xlim()) + max(plt.xlim())) / 2 # Adjust this value to set the y-coordinate of the horizontal line
                        line_color = 'blue'  # Adjust this value to set the color of the line

                        # Plot the horizontal line on top of the image
                        ax.axvline(x=x_coordinate, color=line_color, linestyle='--', linewidth=2)
                        points = plt.ginput(n=1, show_clicks=True, mouse_add=1, mouse_pop=3)
                        self.height = int(abs(self.y - points[0][1]))
                        plt.close()

                else:
                        print("did not process")

        def showFrame(self):
                video = self.video
                threshold_value = self.threshold
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                frame_processed, frame = video.read()

                if frame_processed:
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        _, thresholded = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
                        plt.imshow(thresholded,cmap="gray")
                        plt.show()






                else:
                        print("did not process")
                plt.close()


        def showRectangle(self):
                roi_y = self.y
                roi_width = 1
                roi_height = self.height
                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                roi_x1 = self.x1
                roi_x2 = self.x2
                frame_processed, frame = video.read()
                if frame_processed:





                        # show the x value of where the rectangle would be
                        cv2.rectangle(frame, (roi_x2, roi_y), (roi_x2 + roi_width, roi_y+roi_height), (0, 0, 255), 2)
                        cv2.rectangle(frame, (roi_x1, roi_y), (roi_x1 + roi_width, roi_y+roi_height), (0, 0, 100), 2)
                        plt.imshow(frame)
                        plt.show()

                else:
                        print("did not process")
                plt.close()


        def showCheck(self):
                roi_y = self.y
                roi_width = 1
                roi_height = self.height
                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                roi_x1 = self.x1
                roi_x2 = self.x2
                threshold_value = self.threshold
                frame_processed, frame = video.read()
                if frame_processed:


                        # show the x value of where the rectangle would be
                        cv2.rectangle(frame, (roi_x2, 2), (roi_x2+1, 7), (0, 0, 255), 2)
                        cv2.rectangle(frame, (roi_x1, 2), (roi_x1+1, 7), (0, 0, 100), 2)


                        # Crop the frame to the ROI
                        roi2 = frame[roi_y:roi_y + roi_height, roi_x2:roi_x2 + roi_width]
                        roi1 = frame[roi_y:roi_y + roi_height, roi_x1:roi_x1 + roi_width]

                        # Convert the ROI to grayscale
                        roi2_gray = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
                        roi1_gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)

                        # Threshold the grayscale ROI to detect dark pixels
                        _, thresholded_roi2 = cv2.threshold(roi2_gray, threshold_value, 255, cv2.THRESH_BINARY)
                        _, thresholded_roi1 = cv2.threshold(roi1_gray, threshold_value, 255, cv2.THRESH_BINARY)

                        # Count the number of dark pixels (pixels with value less than threshold)
                        dark_pixel_count2 = cv2.countNonZero(thresholded_roi2)
                        dark_pixel_count1 = cv2.countNonZero(thresholded_roi1)



                        print(f"Pixel Count in ROI1: {dark_pixel_count1}, and ROI2: {dark_pixel_count2}")


        def showDetailedVideo(self):
                roi_y = self.y
                roi_width = 1
                roi_height = self.height
                frame_count = 0
                outside1 = True
                outside2 = True
                initSec = 0
                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                roi_x1 = self.x1
                roi_x2 = self.x2
                threshold_value = self.threshold
                while video.isOpened():
                        frame_processed, frame = video.read()
                        if not frame_processed:
                                break

                        frame_count += 1


                        # show the x value of where the rectangle would be
                        cv2.rectangle(frame, (roi_x2, 2), (roi_x2+1, 7), (0, 0, 255), 2)
                        cv2.rectangle(frame, (roi_x1, 2), (roi_x1+1, 7), (0, 0, 100), 2)
                        plt.imshow(frame)
                        plt.show()

                        user_input = input("Enter 'q' to end the loop: ")
                        if user_input.lower() == 'q':
                                break
                        print(frame.shape)


                        # Crop the frame to the ROI
                        roi2 = frame[roi_y:roi_y + roi_height, roi_x2:roi_x2 + roi_width]
                        roi1 = frame[roi_y:roi_y + roi_height, roi_x1:roi_x1 + roi_width]

                        # Convert the ROI to grayscale
                        roi2_gray = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
                        roi1_gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)

                        # Threshold the grayscale ROI to detect dark pixels
                        _, thresholded_roi2 = cv2.threshold(roi2_gray, threshold_value, 255, cv2.THRESH_BINARY)
                        _, thresholded_roi1 = cv2.threshold(roi1_gray, threshold_value, 255, cv2.THRESH_BINARY)

                        # Count the number of dark pixels (pixels with value less than threshold)
                        dark_pixel_count2 = cv2.countNonZero(thresholded_roi2)
                        dark_pixel_count1 = cv2.countNonZero(thresholded_roi1)
                        plt.imshow(thresholded_roi1, cmap="gray")
                        plt.show()
                        plt.imshow(thresholded_roi2, cmap = "gray")
                        plt.show()

                        if frame_count == 1:
                                initialDarkPixelCount1 = dark_pixel_count1
                                initialDarkPixelCount2 = dark_pixel_count2

                        if dark_pixel_count1 == initialDarkPixelCount1:
                                outside1 = True
                                print("outside1")
                        if dark_pixel_count2 == initialDarkPixelCount2:
                                outside2 = True
                                print("outside2")

                        if dark_pixel_count1 != initialDarkPixelCount1 and outside1:
                                initSec = frame_count
                                print("x1 hit droplet!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                outside1 = False

                        if dark_pixel_count2 != initialDarkPixelCount2 and initSec != 0 and outside2:
                                finalSec = frame_count
                                if finalSec != initSec:
                                        print("x2 hit droplet!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                initSec = 0
                                outside2 = False

                        print(f"Frame {frame_count}: Pixel Count in ROI1: {dark_pixel_count1}, and ROI2: {dark_pixel_count2}")

        def velocityOfDroplet(self,conversion_factor_umeters_per_pixel, conversion_factor_frames_per_second):
                roi_y = self.y
                roi_width = 1
                roi_height = self.height
                frame_count = 0
                velocity = []
                outside1 = True
                outside2 = True
                initSec = 0
                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                roi_x1 = self.x1
                roi_x2 = self.x2
                threshold_value = self.threshold
                while video.isOpened():
                        frame_processed, frame = video.read()
                        if not frame_processed:
                                break

                        frame_count += 1


                        # Crop the frame to the ROI
                        roi2 = frame[roi_y:roi_y + roi_height, roi_x2:roi_x2 + roi_width]
                        roi1 = frame[roi_y:roi_y + roi_height, roi_x1:roi_x1 + roi_width]

                        # Convert the ROI to grayscale
                        roi2_gray = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
                        roi1_gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)

                        # Threshold the grayscale ROI to detect dark pixels
                        _, thresholded_roi2 = cv2.threshold(roi2_gray, threshold_value, 255, cv2.THRESH_BINARY)
                        _, thresholded_roi1 = cv2.threshold(roi1_gray, threshold_value, 255, cv2.THRESH_BINARY)

                        # Count the number of dark pixels (pixels with value less than threshold)
                        dark_pixel_count2 = cv2.countNonZero(thresholded_roi2)
                        dark_pixel_count1 = cv2.countNonZero(thresholded_roi1)

                        if frame_count == 1:
                                initialDarkPixelCount1 = dark_pixel_count1
                                initialDarkPixelCount2 = dark_pixel_count2


                        if dark_pixel_count1 == initialDarkPixelCount1:
                                outside1 = True
                        if dark_pixel_count2 == initialDarkPixelCount2:
                                outside2 = True
                        displacement = roi_x2 - roi_x1

                        if dark_pixel_count1 != initialDarkPixelCount1 and outside1:
                                initSec = frame_count
                                outside1 = False

                        if dark_pixel_count2 != initialDarkPixelCount2 and initSec != 0 and outside2:
                                finalSec = frame_count
                                if finalSec != initSec:
                                        currentVelocity = displacement / (finalSec - initSec)
                                        velocity.append(currentVelocity)
                                initSec = 0
                                outside2 = False


                speed_umeters_per_frame = [speed * conversion_factor_umeters_per_pixel for speed in velocity]
                speed_umeters_per_second = [speed * conversion_factor_frames_per_second for speed in
                                            speed_umeters_per_frame]

                self.velocity = velocity

                # Calculate the mean (average)
                average_speed = np.mean(speed_umeters_per_second)
                self.average_speed = average_speed

                # Calculate the standard deviation
                std_deviation = np.std(speed_umeters_per_second)
                self.std_deviation = std_deviation
        def dropletPerSecond(self, conversion_factor_frames_per_second):
                roi_y = self.y
                roi_width = 1
                roi_height = self.height
                frame_count = 0
                outside1 = True
                outside2 = True
                initSec = 0
                droplet_number = 0
                video = self.video
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                roi_x1 = self.x1
                roi_x2 = self.x2
                threshold_value = self.threshold
                while video.isOpened():
                        frame_processed, frame = video.read()
                        if not frame_processed:
                                break

                        frame_count += 1

                        # Crop the frame to the ROI
                        roi2 = frame[roi_y:roi_y + roi_height, roi_x2:roi_x2 + roi_width]
                        roi1 = frame[roi_y:roi_y + roi_height, roi_x1:roi_x1 + roi_width]

                        # Convert the ROI to grayscale
                        roi2_gray = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
                        roi1_gray = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)

                        # Threshold the grayscale ROI to detect dark pixels
                        _, thresholded_roi2 = cv2.threshold(roi2_gray, threshold_value, 255, cv2.THRESH_BINARY)
                        _, thresholded_roi1 = cv2.threshold(roi1_gray, threshold_value, 255, cv2.THRESH_BINARY)

                        # Count the number of dark pixels (pixels with value less than threshold)
                        dark_pixel_count2 = cv2.countNonZero(thresholded_roi2)
                        dark_pixel_count1 = cv2.countNonZero(thresholded_roi1)

                        if frame_count == 1:
                                initialDarkPixelCount1 = dark_pixel_count1
                                initialDarkPixelCount2 = dark_pixel_count2


                        if dark_pixel_count1 == initialDarkPixelCount1:
                                outside1 = True
                        if dark_pixel_count2 == initialDarkPixelCount2:
                                outside2 = True

                        if dark_pixel_count1 != initialDarkPixelCount1 and outside1:
                                initSec = frame_count
                                droplet_number = droplet_number + 1
                                outside1 = False

                        if dark_pixel_count2 != initialDarkPixelCount2 and initSec != 0 and outside2:
                                initSec = 0
                                outside2 = False


                droplet_flowrate = droplet_number / frame_count
                droplet_flowrate_pers = droplet_flowrate * conversion_factor_frames_per_second
                self.droplet_per_second = droplet_flowrate_pers





