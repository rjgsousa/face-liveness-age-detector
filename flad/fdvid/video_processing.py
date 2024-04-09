import streamlit as st

import cv2
from flad.fdspoof.face_detection_spoofing import FaceDetectionSpoofing


class VideoProcessing(FaceDetectionSpoofing):

    def __init__(self, video_file_path, output_file_path=None):
        super().__init__()
        self.video_file_path = video_file_path
        self.output_file_path = output_file_path
        self.do_preview = True

        self.cap = cv2.VideoCapture(self.video_file_path)

        if self.output_file_path is not None:
            self.do_preview = False
            self._prep_save_to_disk()

    def detect(self):

        while True:
            ret, frame = self.cap.read()

            suc_state, res_frame = self.detect_face_and_spoof(frame, preview_it=self.do_preview)
            if suc_state:
                self.video_writer.write(res_frame)

            if self.do_preview:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        self.cap.release()
        if not self.do_preview:
            self.video_writer.release()
        cv2.destroyAllWindows()

    def _prep_save_to_disk(self):
        # Get video properties
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # specify a writer to write a processed video to a disk frame by frame
        fourcc_mp4 = cv2.VideoWriter_fourcc(*'mp4v')

        self.video_writer = cv2.VideoWriter(self.output_file_path, fourcc_mp4, fps, (width, height))
