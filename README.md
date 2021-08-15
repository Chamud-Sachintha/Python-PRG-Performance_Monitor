<h1>Performance Monitor</h1>

<h2>Introduction</h2>
Performance Monitor (PerfMon) is a tool that comes built-in with Windows and allows you to look into the performance of your system and the applications that are running on it.  
It gives you a way to view data points that are associated with these applications and link them with the effect they have on your system.  
You can monitor data points both in real-time or collect them for analysis at a later time.  
Collection can also be scheduled for specific times of the day if there are only specific windows of time where you are experiencing an issue that you would like to monitor.  
Another important thing to note with the tool is it can also be used to monitor remote servers, not just the local server where the tool is running.

<h2>Explanation</h2>
From the system perspective there are performance counters that can help you to identify a wide range of system bottlenecks.  
There are counters related to disk performance, both physical and logical through put on both the adapter and all interfaces, CPU, memory and a host of other subsystems that run on top of your operating system.  
If you are running Hyper-V there are also counters specifically related to all of its resources.
<ol>
  <li>Using Performance Monitor</li>
  <ul>
    <li>Access to Windows Performance Monitor features</li>
    <li>Launching the application</li>
  </ul>
  <li>Methods for collecting data</li>
  <ul>
    <li>Real-time data collection</li>
    <li>Creating a new collector set</li>
  </ul>
  <li>Data Collection</li>
  <ul>
    <li>On demand</li>
    <li>Scheduled</li>
  </ul>
  <li>Display/Report collected data</li>
  <ul>
    <li>Using Perfmon</li>
    <li>Using a spreadsheet</li>
  </ul>
</ol>

<h2>Installation</h2>
<ul>
  <li>First Downlaod The Script files in this repository or clone the scripts.</li>
  <li>Make Sure You Have Python 3 installed and required Libraries.</li>
  <li>After that Open Powershell and set the working directory to script's path.</li>
  <li>and then type "python -u "PerformanceMonitor_Main.py"" and hit enter.</li>
  <li>You can available setup file in this web site <a href="http://www.mydev.22web.org">www.mydev.22web.org</a></li>
