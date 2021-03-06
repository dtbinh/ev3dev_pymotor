import cv2
import time
import picamera
import picamera.array

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320, 240)
        #camera.framerate = 30
        # Wait for the automatic gain control to settle
        time.sleep(2)
        # Now fix the values
        #camera.shutter_speed = camera.exposure_speed
        #camera.exposure_mode = 'off'
        #g = camera.awb_gains
        #camera.awb_mode = 'off'
        #camera.awb_gains = g

        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            # stream.array now contains the image data in BGR order
            cv2.imshow('frame', stream.array)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # reset the stream before the next capture
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()
