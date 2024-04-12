
Project Overview
################

Face Liveness and Age Detector (FLAD) project is a computer vision system designed to detect and analyze faces in images and videos. The primary goals of the project are to determine the authenticity of detected faces (i.e., whether they are spoofed or genuine, usually referred as liveness detection) and to estimate the age of the individuals in the images or videos.

It should be mentioned that this project is currently in its early stages of development, focusing on creating an end-to-end Proof of Concept (PoC) to demonstrate the feasibility of the proposed goals. At this stage, the project leverages the `InsightFace <https://insightface.ai/>`_ package, a state-of-the-art face recognition and analysis library, to expedite the development process and validate our approach. However, it is important to note that this is just the beginning, and there is still a significant amount of work to be done to refine the algorithms, improve accuracy, and optimize performance.

By utilizing the InsightFace package, we can take advantage of its pre-trained models and robust algorithms for face and liveness detection.

.. _flad_structure:

Project Structure
=================

Face, Liveness and Age Detection
--------------------------------

``FaceDetectionSpoofing`` class is a key component of the Face Liveness and Age Detector (FLAD) project. It provides functionality for detecting and identifying faces in an image and determining if the detected faces are spoofed or genuine.

    .. autoclass:: flad.fdspoof.face_detection_spoofing.FaceDetectionSpoofing
        :members:

The main method of this class is ``detect_face_and_spoof``, which takes an image as input, either as a file path or a NumPy array. It processes the image to detect faces and applies spoofing detection algorithms to determine the authenticity of each detected face. The ``detect_face_and_spoof`` method returns a tuple containing a boolean value indicating the success of the operation and the processed image as a NumPy array. It also has an optional parameter *preview_it*, which allows the user to choose whether to preview the resulting frame or prioritize saving it to disk.

Overall, the ``FaceDetectionSpoofing`` class encapsulates the core functionality of face detection and spoofing detection, making it a crucial part of the FLAD project. It can be used independently or as a base class for more specialized classes, such as the VideoProcessing class, which extends its capabilities to handle videos.

Video Processing
----------------

The :class:`VideoProcessing` class extends the functionality of the :class:`FaceDetectionSpoofing` class. It processes a video frame by frame, applying face detection, liveness detection, and age estimation algorithms to each frame as aforementioned described. The class initializes with the path to the input video file and an optional output file path.

    .. autoclass:: flad.fdvid.video_processing.VideoProcessing
        :members:


Results and Discussion
######################

When we started this project, we explored various computer vision techniques for face detection, including algorithms such as Haar cascades, which are commonly used in conjunction with age estimation models like regression or classification-based methods. Initially, we implemented face detection using the OpenCV Haar cascade classifier, as it is one of the simplest and most straightforward approaches available. However, and as expected, during the early stages of development, we encountered a significant number of false positive detections, indicating that the Haar cascade method alone was not sufficient for our requirements.

Regarding age and gender estimation, we initially incorporated the principled approach described by Rothe et al. in their 2015 ICCVW paper :cite:p:`Rothe-ICCVW-2015`. Their method leverages convolutional neural networks (CNNs), such as the VGG-16 architecture, which are pretrained on the ImageNet dataset for image classification tasks and reformulate the age regression problem as a deep classification problem. Yet, when we implemented this method, we observed considerable latencies in processing images, resulting in a noticeably low frames per second (FPS) rate, which could potentially hinder real-time performance. Another challenge is that it does not tackles liveness/spoofing.

It is important to highlight that we were conscious of the different limitations of each of the methods listed above. We recognize that building a strong case study from scratch would provide a deeper understanding of the underlying techniques and allow for more freedom in incorporating future developments, such as novel machine learning test beds for benchmarks. However, given the time constraints of this project, we opted to pursue a more straightforward approach that could yield high-quality results within the available timeframe.

While developing a custom solution from the ground up would have been ideal, we understood that it would require significant time and resources to achieve the desired level of performance. Therefore, we made a pragmatic decision to leverage existing state-of-the-art methods and libraries, such as the InsightFace package, which has been extensively tested and optimized for face recognition, liveness and age detection.

To benchmark our initial results, we leveraged the vast data available on the `This Person Does Not Exist <thispersondoesnotexist.com>`_ website. We downloaded a set of images from this site and processed them through our Face Liveness and Age Detector (FLAD) system. Below, we present a comparison between the original image, and the corresponding output.

.. list-table::

    *   - .. figure :: images/person_does_not_exist_0001.jpeg

            Figure: Original image (which is a person that does not exist).

        - .. figure :: images/person_does_not_exist_0001_res.jpeg

            Figure: FLAD output (red frame highlight that this is not a real person as it is below a given threshold).


In addition to the thispersondoesnotexist.com dataset, we also evaluated FLAD's performance using images from public benchmarks, such as the `"Labeled Faces in the Wild" (LFW) <https://vis-www.cs.umass.edu/lfw/>`_ dataset. The image provided shows a sample output from our FLAD system, demonstrating its ability to accurately detect and analyze faces. The system successfully identifies the presence of a face in the image and provides estimates for age and gender.

.. list-table::

    *   - .. figure :: images/Jim_OBrien_0002.jpg

            Figure: Original image (Jim O'Brien from LFW)

        - .. figure ::  images/Jim_OBrien_0002_res.jpg

            Figure: FLAD output

        - .. figure ::  images/Jim_OBrien_0002_deep_funneled_res.jpg

            Figure: FLAD output on a Deep Funneled image from Jim O'Brien.

By testing our system on both the thispersondoesnotexist.com dataset and LFW, we aimed to assess its robustness and generalization capabilities across different types of images. The thispersondoesnotexist.com dataset provided a large volume of high-quality, synthetically generated face images, allowing us to evaluate FLAD's performance on a controlled and consistent set of samples. On the other hand, the LFW dataset offered a more challenging and realistic scenario, with face images captured in various lighting conditions, poses, and backgrounds.


FLAD: Workflow
##############

This figure illustrates the end-to-end workflow of the Face Liveness and Age Detector project.

.. figure:: images/FLAD-workflow.png
    :name: FLAD_workflow_fig

    Figure: Workflow of the Face Liveness and Age Detector (FLAD)

The FLAD project has potential applications in various domains, including security systems, access control, user authentication, and demographic analysis. By providing reliable face detection, liveness detection, and age estimation capabilities, the project can contribute to the development of more secure and intelligent computer vision systems.

