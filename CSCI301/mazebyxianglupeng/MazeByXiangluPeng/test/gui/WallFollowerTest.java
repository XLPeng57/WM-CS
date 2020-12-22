


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
public class WallFollowerTest extends WallFollower {

	
	WallFollower wallfollower;
	ReliableRobot robot;
	Controller controller;
	Maze maze;
	
	@Before
	public void setUp() {	
		
		robot = new ReliableRobot(controller);	
		controller = new Controller();
		wallfollower = new WallFollower();
		wallfollower.setRobot(robot);	
		wallfollower.setMaze(controller);
		
		controller.setFileName("test/data/input.xml");
		controller.setRobotAndDriver(robot, wallfollower);
		
		controller.start();
		controller.turnOffGraphics();
		maze = controller.getMazeConfiguration();
		controller.switchFromGeneratingToPlaying(maze);
		robot.setController(controller);
		wallfollower.setMaze(controller);
		


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
		wallfollower.drive2Exit();
		assertTrue(robot.isAtExit());
		assertEquals(true, wallfollower.drive2Exit());
	}
	
	
	




}
