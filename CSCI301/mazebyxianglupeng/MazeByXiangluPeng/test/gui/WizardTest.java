


package gui;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

import generation.CardinalDirection;
import generation.Maze;
import gui.Robot.Turn;

/**
 * 
 * @author Xianglu Peng
 *
 */
public class WizardTest extends Wizard {

	
	Wizard wizardDriver;
	ReliableRobot robot;
	Controller controller;
	Maze maze;
	
	@Before
	public void setUp() {	
		
		robot = new ReliableRobot(controller);	
		controller = new Controller();
		wizardDriver = new Wizard();
		wizardDriver.setRobot(robot);	
		wizardDriver.setMaze(controller);
		
		controller.setFileName("test/data/input.xml");
		controller.setRobotAndDriver(robot, wizardDriver);
		
		controller.start();
		controller.turnOffGraphics();
		maze = controller.getMazeConfiguration();
		controller.switchFromGeneratingToPlaying(maze);
		robot.setController(controller);
		wizardDriver.setMaze(controller);
		


	}
	
	
	/**
	 * Test case: Check if the wizarddriver drive the robot to the exit  
	 * <p>
	 * Method under test: drive2Exit(), isAtExit()
	 * <p>
	 * Correct behavior: Check if the robot is at the exit finally.
	 * 
	 */
	
	@Test
	public final void testDrive2Exit() throws Exception {
		setUp();
		wizardDriver.drive2Exit();
		assertTrue(robot.isAtExit());
		assertEquals(true, wizardDriver.drive2Exit());
	}
	
	
	




}
