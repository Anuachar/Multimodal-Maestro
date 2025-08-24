<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Multimodal Cursor Controller</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background: #f9f9f9;
    }

    /* Navbar */
    .navbar {
      background-color: #0066cc;
      overflow: hidden;
    }
    .navbar a {
      float: left;
      display: block;
      color: white;
      text-align: center;
      padding: 14px 20px;
      text-decoration: none;
    }
    .navbar a:hover {
      background-color: #004d99;
    }

    /* Page content */
    .container {
      padding: 20px;
    }

    h2 {
      color: #333;
    }

    .section {
      background: #e6f0fa;
      margin: 20px 0;
      padding: 20px;
      border-radius: 5px;
    }

    /* Buttons */
    .btn {
      background-color: #0066cc;
      border: none;
      color: white;
      padding: 12px 20px;
      margin: 10px;
      cursor: pointer;
      font-size: 14px;
      border-radius: 4px;
    }
    .btn:hover {
      background-color: #004d99;
    }

    .button-group {
      margin-top: 15px;
    }
  </style>
</head>
<body>

  <!-- Navbar -->
  <div class="navbar">
    <a href="#">Home</a>
    <a href="#">About App</a>
    <a href="#">Team Members</a>
  </div>

  <!-- Main Content -->
  <div class="container">
    <h1>Multimodal Cursor Controller</h1>

    <div class="section">
      <h2>Control Your Cursor Using Hand Gestures</h2>
      <p>
        The Hand Controller allows users to control their computer using simple hand gestures, 
        offering accessibility and ease of use.
      </p>
      <div class="button-group">
        <button class="btn">Start Hand Controller</button>
        <button class="btn">Stop Hand Controller</button>
      </div>
    </div>

    <div class="section">
      <h2>Control Your Cursor Using Eye Gaze</h2>
      <p>
        The Gaze Controller enables cursor movement and clicks using eye gaze and blinks, 
        ideal for hands-free interaction.
      </p>
      <div class="button-group">
        <button class="btn">Start Gaze Controller</button>
        <button class="btn">Stop Gaze Controller</button>
      </div>
    </div>
  </div>

</body>
</html>
