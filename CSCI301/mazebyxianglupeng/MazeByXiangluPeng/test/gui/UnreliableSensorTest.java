package gui;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Before;
import org.junit.Test;

import generation.CardinalDirection;
import generation.Maze;
import gui.Robot.Direction;

public class UnreliableSensorTest extends UnreliableSensor {

	
	UnreliableSensor sensor;
	Controller controller;
	WallFollower wallfollower;
	UnreliableRobot robot;
	Maze maze;
	
	@Before
	public void setUp() {
		
		
		controller = new Controller();	
		sensor = new UnreliableSensor();
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
	
	/**
	 * Test case: Check the set sensor direction method 
	 * <p>
	 * Method under test: setSensorDirection(Direction.LEFT)
	 * <p>
	 * Correct behavior: The cardinal direction are set accordingly
	 * 
	 */
	
	@Test
	public final void testsetSensorDirection() throws Exception {

		
		assertEquals(controller.getCurrentDirection(),CardinalDirection.East);
		CardinalDirection cd = controller.getCurrentDirection();
		sensor.setSensorDirection(Direction.LEFT);
		cd = sensor.cd;
		assertEquals(cd,CardinalDirection.North);
	
		sensor.setSensorDirection(Direction.RIGHT);
		cd = sensor.cd;
		assertEquals(cd,CardinalDirection.South);
		
		sensor.setSensorDirection(Direction.FORWARD);
		cd = sensor.cd;
		assertEquals(cd,CardinalDirection.East);
		
		sensor.setSensorDirection(Direction.BACKWARD);
		cd = sensor.cd;
		assertEquals(cd,CardinalDirection.West);
		
		
	}
	
	
//	@Test
//	public final void testsetSensorFailure() throws Exception {
//
//		assertTrue(sensor.operational);
//		sensor.startFailureAndRepairProcess(4000, 2000);
//		//Thread.sleep(4000);
//		assertEquals(sensor.operational, false);
//		
//	}
	
	

	
	
	
}
