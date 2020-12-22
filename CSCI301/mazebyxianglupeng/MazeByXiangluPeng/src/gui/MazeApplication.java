/**
 * 
 */
package gui;

import generation.Order;

import java.awt.event.KeyListener;
import java.io.File;

import javax.swing.JFrame;


/**
 * This class is a wrapper class to startup the Maze game as a Java application
 * 
 * This code is refactored code from Maze.java by Paul Falstad, www.falstad.com, Copyright (C) 1998, all rights reserved
 * Paul Falstad granted permission to modify and use code for teaching purposes.
 * Refactored by Peter Kemper
 * 
 * TODO: use logger for output instead of Sys.out
 */
public class MazeApplication extends JFrame {

	// not used, just to make the compiler, static code checker happy
	private static final long serialVersionUID = 1L;

	/**
	 * Constructor
	 */
	public MazeApplication() {
		init(null,null,null);
	}

	/**
	 * Constructor that loads a maze from a given file or uses a particular method to generate a maze
	 * @param parameter can identify a generation method (Prim, Kruskal, Eller)
     * or a filename that stores an already generated maze that is then loaded, or can be null
	 */
	public MazeApplication(String builder, String driver, String sensor) {
		init(builder,driver,sensor);
	}

	/**
	 * Instantiates a controller with settings according to the given parameter.
	 * @param parameter can identify a generation method (Prim, Kruskal, Eller)
	 * or a filename that contains a generated maze that is then loaded,
	 * or can be null
	 * @return the newly instantiated and configured controller
	 */
	 Controller createController(String builder, String driver, String sensor) {
	    // need to instantiate a controller to return as a result in any case
	    Controller result = new Controller() ;
	    // can decide if user repeatedly plays the same mazes or 
	    // if mazes are different each and every time
	    // set to true for testing purposes
	    // set to false for playing the game
	    result.setDeterministic(false);
	    String buildermsg = null;
	    String drivermsg = null;
	    String sensormsg = null;
	    // message for feedback
	    // Case 1: no input
	    if (builder == null) {
	    	buildermsg = "MazeApplication: maze will be generated with a randomized algorithm."; 
	    }
	    // Case 2: Prim
	    else if ("Prim".equalsIgnoreCase(builder))
	    {
	    	buildermsg = "MazeApplication: generating random maze with Prim's algorithm.";
	        result.setBuilder(Order.Builder.Prim);
	    }
	    // Case 3 a and b: Eller, Kruskal or some other generation algorithm
	    else if ("Kruskal".equalsIgnoreCase(builder))
	    {
	    	// TODO: for P2 assignment, please add code to set the builder accordingly
	    	result.setBuilder(Order.Builder.Kruskal);
	        //throw new RuntimeException("Don't know anybody named Kruskal ...");
	    }
	    else if ("Eller".equalsIgnoreCase(builder))
	    {
	    	// TODO: for P2 assignment, please add code to set the builder accordingly
	    	buildermsg = "MazeApplication: generating random maze with Eller's algorithm.";
	    	result.setBuilder(Order.Builder.Eller);
	        //throw new RuntimeException("Don't know anybody named Eller ...");
	    }
//	    else if ("Wizard".equalsIgnoreCase(parameter))
//	    {
//	    	msg = "MazeApplication: using wizard";
//	    	result.setBuilder(Order.Builder.DFS);
//	    	Robot robot = new ReliableRobot();
//	    	Wizard wizardDriver = new Wizard();
//	    	wizardDriver.setRobot(robot);
//	    	result.setRobotAndDriver(robot, wizardDriver);
//	    	wizardDriver.setMaze(result);
//	    	
//	    
//	    }
	    // Case 4: a file
	    else {
	         File f = new File(builder) ;
	         if (f.exists() && f.canRead())
	         {
	             buildermsg = "MazeApplication: loading maze from file: " + builder;
	             result.setFileName(builder);
	             return result;
	         }
	         else {
	             // None of the predefined strings and not a filename either: 
	             buildermsg = "MazeApplication: unknown parameter value: " + builder + " ignored, operating in default mode.";
	         }
	     }
	    
	    
	    Robot robot;
	    
	   

	    
	    if (driver == null) {
	    	drivermsg = "MazeApplication: maze will be drived manually.";
	    }

	    if ("Wizard".equalsIgnoreCase(driver)) {
	    	
	    	if (sensor == null || sensor.equalsIgnoreCase("1111")) {
	    		robot = new ReliableRobot();
	    		
	    	}else {
	    		
	    		char L,R,B,F;
	    		F = sensor.charAt(0);
	    		L = sensor.charAt(1);
	    		R = sensor.charAt(2);
	    		B = sensor.charAt(3);
	    	    robot = new UnreliableRobot(result,F,L,R,B);
	    	
	    		
	    	}
	    	drivermsg = "MazeApplication: using wizard";
	    	Wizard wizardDriver = new Wizard();
	    	wizardDriver.setRobot(robot);
	    	result.setRobotAndDriver(robot, wizardDriver);
	    	wizardDriver.setMaze(result);
	    }
	    
	    if ("WallFollower".equalsIgnoreCase(driver)) {
	    	

	    	if (sensor == null) {
	    		robot = new ReliableRobot(result);
	    		
	    	}else {
	    	
	    		char L,R,B,F;
	    		F = sensor.charAt(0);
	    		L = sensor.charAt(1);
	    		R = sensor.charAt(2);
	    		B = sensor.charAt(3);
	    	    robot = new UnreliableRobot(result,F,L,R,B);
	    	
	    		
	    	}
	    	drivermsg = "MazeApplication: using wallfollower";
	    	WallFollower wallDriver = new WallFollower();
	    	wallDriver.setRobot(robot);
	    	result.setRobotAndDriver(robot, wallDriver);
	    	wallDriver.setMaze(result);
	    	
	    }
	    
	    
	    
	    
	   
	    // controller instanted and attributes set according to given input parameter
	    // output message and return controller
	    System.out.println(buildermsg);
	    System.out.println(drivermsg);
	    System.out.println(sensormsg);
	    return result;
	}

	/**
	 * Initializes some internals and puts the game on display.
	 * @param parameter can identify a generation method (Prim, Kruskal, Eller)
     * or a filename that contains a generated maze that is then loaded, or can be null
	 */
	private void init(String builder, String driver, String sensor) {
	    // instantiate a game controller and add it to the JFrame
	    Controller controller = createController(builder,driver,sensor);
		add(controller.getPanel()) ;
		// instantiate a key listener that feeds keyboard input into the controller
		// and add it to the JFrame
		KeyListener kl = new SimpleKeyListener(this, controller) ;
		addKeyListener(kl) ;
		// set the frame to a fixed size for its width and height and put it on display
		setSize(Constants.VIEW_WIDTH, Constants.VIEW_HEIGHT+22) ;
		setVisible(true) ;
		// focus should be on the JFrame of the MazeApplication and not on the maze panel
		// such that the SimpleKeyListener kl is used
		setFocusable(true) ;
		// start the game, hand over control to the game controller
		controller.start();
	}
	
	/**
	 * Main method to launch Maze game as a java application.
	 * The application can be operated in three ways. 
	 * 1) The intended normal operation is to provide no parameters
	 * and the maze will be generated by a randomized DFS algorithm (default). 
	 * 2) If a filename is given that contains a maze stored in xml format. 
	 * The maze will be loaded from that file. 
	 * This option is useful during development to test with a particular maze.
	 * 3) A predefined constant string is given to select a maze
	 * generation algorithm, currently supported is "Prim".
	 * @param args is optional, first string can be a fixed constant like Prim or
	 * the name of a file that stores a maze in XML format
	 */
	public static void main(String[] args) {
		
		JFrame app ; 
	    int i = 0;
	    String commmand, builder = null, driver = null, sensor = null;
	    
	    if (args.length == 0) {
	    	app = new MazeApplication();
	    }
	    
	    while (i < args.length && args[i].startsWith("-")) {
	    	commmand = args[i++];
	    	
	   
	    	if (commmand.equals("-g")) {

	    		commmand = args[i++];
	    		
	    		if (commmand.equalsIgnoreCase("Prim")) {
	    			builder = "Prim";
	    		}
	    		else if (commmand.equalsIgnoreCase("Eller")) {
	    			builder = "Eller";
	    		}
	    		
	    		else if (commmand.equalsIgnoreCase("DFS")) {
	    			builder = "DFS";
	    		}
	    		else {
	    			builder = commmand;
	    		}
	    		
	    	}
	    	
	  
	    	if (commmand.equals("-d")) {

	    		commmand = args[i++];
	    		
	    		if (commmand.equalsIgnoreCase("Wizard")) {
	    			driver = "Wizard";
	    		}
	    		
	    		if (commmand.equalsIgnoreCase("Wallfollower")) {
	    			driver = "Wallfollower";
	    		}
	    		
	    		if (commmand.equalsIgnoreCase("Manual")) {
	    			driver = null;
	    		}
	    		
	    		if (!commmand.equalsIgnoreCase("Wizard") &&
	    			!commmand.equalsIgnoreCase("Wallfollower") && !commmand.equalsIgnoreCase("Manual") ) {
	    			System.out.println("Not supported builder");
	    			System.exit(0);
	    		}
	    	}
	    	
	    	
	    	if (commmand.equals("-r")) {
	    		
	    		commmand = args[i++];
	    		if (commmand.length() == 4) {
	    			for(int j=0; j<4; j++) {
		    			if (commmand.charAt(j) == '0' || commmand.charAt(j) == '1') {
		    				;
		    			}else {
		    				System.out.println("Not supported sensor");
			    			System.exit(0);
		    			}
		    		}
	    		}else {
	    			System.out.println("Not supported sensor");
	    			System.exit(0);
	    		}	
	    		
	    		sensor = commmand;
	    	}
	    
	    }
	   
	    
	    app = new MazeApplication(builder, driver, sensor);
		app.repaint() ;
	}


		


}
