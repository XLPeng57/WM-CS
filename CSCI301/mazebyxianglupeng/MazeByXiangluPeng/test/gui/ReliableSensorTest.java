package gui;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertNotEquals;

import org.junit.Before;
import org.junit.Test;

import generation.CardinalDirection;
import generation.Maze;
import gui.Robot.Direction;
import gui.Robot.Turn;

public class ReliableSensorTest extends ReliableSensor {

	
	ReliableSensor sensor;
	Controller controller;
	Maze maze;
	
	@Before
	public void setUp() {
		controller = new Controller();	
		sensor = new ReliableSensor();
		controller.setFileName("test/data/input.xml");			
		controller.start();
		controller.turnOffGraphics();
		maze = controller.getMazeConfiguration();
		controller.switchFromGeneratingToPlaying(maze);
		maze = controller.getMazeConfiguration();
		sensor.setController(controller);
	}
	
	
	
	/**
	 * Test case: Check if the getEnergyConsumptionForSensing method is working properly 
	 * <p>
	 * Method under test:getEnergyConsumptionForSensing()
	 * <p>
	 * Correct behavior: Moved the robot in a room manually, then check if it is in the room.
	 * 
	 */
	@Test
	public final void testgetEnergyConsumptionForSensing() throws Exception {

		assertTrue(sensor.getEnergyConsumptionForSensing() == 1f);
		
	}
	
	
	/**
	 * Test case: Check The starting point of the maze 
	 * <p>
	 * Method under test: maze.getStartingPosition()
	 * <p>
	 * Correct behavior: The starting point should be (4,0)
	 * 
	 */
	@Test
	public final void testStartingPoint() throws Exception {

		int x, y;
		x = maze.getStartingPosition()[0];
		y = maze.getStartingPosition()[1];
		assertEquals(x, 4);
		assertEquals(y, 0);
	
		
	}
	
	@Test
	public final void testDistanceToObstacle() throws Exception {

		int[] cur_pos = maze.getStartingPosition();
		float s = 3500;
		float[] array = new float[1];
		array[0] = s;
		
		int dis_forward = sensor.distanceToObstacle(cur_pos, CardinalDirection.East,array);
		assertEquals(dis_forward,11);
		
	
		
	}
	
	

	
	
	
}
