import argparse

from flad.fdvid.video_processing import VideoProcessing
from flad.fdspoof.face_detection_spoofing import FaceDetectionSpoofing


def exec_test(img_file_path):
    fd = FaceDetectionSpoofing()
    fd.detect_face_and_spoof(img_file_path)


def main(arguments):
    video_file_path = arguments.video_file_path
    output_file_path = arguments.output_file_path

    if arguments.img_file_path is not None:
        exec_test(arguments.img_file_path)
    else:
        flad = VideoProcessing(video_file_path, output_file_path)
        flad.detect()


if __name__ == "__main__":
    #
    parser = argparse.ArgumentParser()

    parser.add_argument("--video-file-path",
                        default="data/external/Faces from around the world.mp4", type=str,
                        help="folder for the data from web")
    parser.add_argument("--output-file-path", type=str, help="output results")

    spoofing_args = parser.add_argument_group('arguments for face spoofing')
    spoofing_args.add_argument("--img-file-path", type=str,
                               help="folder for the data from web")

    args = parser.parse_args()

    main(args)
