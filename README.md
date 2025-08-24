# Multimodal-Maestro
“Virtual mouse using gaze and hand gestures"


Multimodal Maestro is an AI-powered virtual mouse system that enables hands-free interaction with computers using hand gestures and eye gaze tracking.
The project is specially designed for accessibility applications, empowering disabled individuals to control a computer without relying on traditional input devices.



Features : 

 Hand Gesture Controller – Real-time cursor control using intuitive hand gestures.

Eye Gaze Controller – Cursor movement and clicks through gaze tracking & blink detection.

Accessibility-Focused – Designed to support individuals with limited motor abilities.

Optimized Performance – Real-time response using CNNs and gaze tracking pipelines.

The project was trained & tested on eye images and hand gesture datasets.


Project Overview : 


Multimodal Maestro is a vision-based human–computer interaction (HCI) framework that integrates hand gesture recognition and eye gaze tracking into a unified control system. The model was trained and validated on live-streamed video data captured via a standard webcam, where both eye movement sequences and hand gestures were recorded in real time.

The training pipeline leverages deep convolutional neural networks (CNNs) for gesture classification and landmark-based gaze estimation models for pupil tracking and blink detection. These modalities were fused to provide robust and adaptive cursor control in unconstrained environments.

Unlike conventional input devices, this system eliminates the dependency on physical hardware (mouse/keyboard), making it especially valuable for accessibility applications. The primary design motivation was to assist disabled and motor-impaired individuals, providing them with an intuitive, hands-free interface to operate a computer.




Key highlights include:

Real-Time Performance → Optimized inference with CNNs and lightweight gaze estimators allows seamless operation via webcam.

Accessibility-Driven Design → Specifically tailored for individuals with paralysis, limb disabilities, or limited motor control.

Multimodal Fusion → Eye gaze is mapped to cursor coordinates, while blinks trigger selection actions. Hand gestures act as complementary controllers for navigation.

Practical Deployment → Can run on consumer-grade hardware without requiring specialized sensors, ensuring wider usability.

This approach demonstrates how AI-driven multimodal systems can transform traditional computing into a more inclusive technology, bridging the gap between advanced ML research and real-world assistive applications.




