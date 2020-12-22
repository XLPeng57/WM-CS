package gui;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;

import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;

import generation.CardinalDirection;
import generation.Maze;
import gui.Robot.Turn;

public class ReliableRobotTest extends ReliableRobot {
	
	Robot robot;
	Wizard wizardDriver;
	Controller controller;
	Maze maze;
	
	@Before
	public void setUp() {
		
		//robot = new ReliableRobot(controller);	
		controller = new Controller();
		wizardDriver = null;	
		
		controller.setFileName("test/data/input.xml");
		controller.setRobotAndDriver(robot, wizardDriver);		
		controller.start();
		controller.turnOffGraphics();
		
		maze = controller.getMazeConfiguration();
		controller.switchFromGeneratingToPlaying(maze);
		robot = new ReliableRobot(controller);	
		robot.setController(controller);
		
	}

	
	

	/**
	 * Test case: Check the starting point of the robot
	 * <p>
	 * Method under test: getCurrentPosition(), getCurrentDirection(), getBatteryLevel()
	 * <p>
	 * Correct behavior: Starting point is (4,0), starting direction is East,
	 * starting battery is 3500.
	 */
	
	@Test
	public final void testStartingPoint() throws Exception {

		int x, y;
		x = robot.getCurrentPosition()[0];
		y = robot.getCurrentPosition()[1];
		assertEquals(x, 4);
		assertEquals(y, 0);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.East);
		assertTrue(robot.getBatteryLevel() == 3500f);
		
	}

	
	/**
	 * Test case: Checks the rotate method is working properly
	 * <p>
	 * Method under test: getCurrentPosition(), getCurrentDirection(), getBatteryLevel(), rotate()
	 * <p>
	 * Correct behavior: The current position should not chagne. 
	 * The battery level should decrease the correct value each time.
	 * The currentDirection should change accordingly
	 */
	@Test
	public final void testRotate() throws Exception {
		
		
		assertEquals(robot.getCurrentPosition()[0], 4); 
		assertEquals(robot.getCurrentPosition()[1], 0);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.East);
		assertTrue(robot.getBatteryLevel() == 3500f);
			
		robot.rotate(Turn.LEFT);
		assertEquals(robot.getCurrentPosition()[0], 4);  
		assertEquals(robot.getCurrentPosition()[1], 0); 
		assertTrue(robot.getBatteryLevel() == 3497f);
		assertEquals(robot.getCurrentDirection(), CardinalDirection.North);
		
		robot.rotate(Turn.RIGHT);
		assertEquals(robot.getCurrentPosition()[0], 4); 
		assertEquals(robot.getCurrentPosition()[1], 0); 
		assertEquals(robot.getCurrentDirection(), CardinalDirection.East);
		assertTrue(robot.getBatteryLevel() == 3494f);
		
		robot.rotate(Turn.AROUND);
		assertEquals(robot.getCurrentPosition()[0], 4); 
		assertEquals(robot.getCurrentPosition()[1], 0); 
		assertEquals(robot.getCurrentDirection(),CardinalDirection.West);
		assertTrue(robot.getBatteryLevel() == 3488f);
	}

	
	/**
	 * Test case: Check if the move method is working properly and the robot stopped if it hitted the wall. 
	 * <p>
	 * Method under test: hasStopped(), getBatteryLevel(), rotate(), move(), getCurrentPosition(), getCurrentDirection()
	 * <p>
	 * Correct behavior: The starting point is (4,0), when the robot moved one step, the current position is (5,0)
	 * The battery level decreased by 6. Then, rotate the robot and let it move into a wall to see if the robot stopped. 
	 */

	@Test
	public final void testMove1StepAndHitTheWall() throws Exception {		
		
		assertEquals(robot.getOdometerReading(),0);	
		assertEquals(robot.getCurrentPosition()[0],4);  
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(CardinalDirection.East,robot.getCurrentDirection());
		assertTrue(robot.getBatteryLevel() == 3500f);

		//Move one step
		robot.move(1);
		assertEquals(robot.getCurrentPosition()[0],5);
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.East);
		assertTrue(robot.getBatteryLevel() == 3494f);
		
		
		//Rotate, face the wall, move
		//The robot should stop
		robot.rotate(Turn.RIGHT);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.South);
		robot.move(1);
		assertEquals(robot.getCurrentPosition()[0],5); 
		assertEquals(robot.getCurrentPosition()[1],0); 
		assertTrue(robot.getBatteryLevel() == 3491f);
		assertTrue(robot.hasStopped());
	}
	
	
	/**
	 * Test case: Check if the robot stopped when it ran out of energy
	 * <p>
	 * Method under test: hasStopped(), getBatteryLevel(), rotate()
	 * <p>
	 * Correct behavior: The hasStopped should be true at the beginning. And when the robot 
	 * did not have enough battery, hasStppoed = false
	 * @throws Exception 
	 */
	@Test
	public final void testInsufficientBatteryStop() throws Exception {
		
		
		assertFalse(robot.hasStopped());
		assertTrue(robot.getBatteryLevel() == 3500f);
		robot.setBatteryLevel(2f);
		assertTrue(robot.getBatteryLevel() == 2f);
		robot.rotate(Turn.LEFT);
		assertTrue(robot.hasStopped());
		
	}
	
	

	/**
	 * Test case: Check if the odometer is working properly after moving and resetting 
	 * <p>
	 * Method under test: getBatteryLevel(), move(), getCurrentPosition(), 
	 * getCurrentDirection(), getOdometerReading(),GetOdometerReading()
	 * <p>
	 * Correct behavior: The robot move 1 step, the odometer reading should be 1;
	 * After resetting the odometer, the reading should be 0
	 */
	
	@Test
	public final void testOdometerWorking() throws Exception {		
		
		//starting point
		assertEquals(robot.getOdometerReading(),0);	
		assertEquals(robot.getCurrentPosition()[0],4);  
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(CardinalDirection.East,robot.getCurrentDirection());
		assertTrue(robot.getBatteryLevel() == 3500f);

		//move one step and check odometer raeding
		robot.move(1);
		assertEquals(robot.getCurrentPosition()[0],5);
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.East);
		assertTrue(robot.getBatteryLevel() == 3494f);
		assertEquals(robot.getOdometerReading(),1);
		
		//reset odometer
		robot.resetOdometer();
		assertEquals(robot.getOdometerReading(),0);
	}
	

	/**
	 * Test case: Check if the jump method is working properly 
	 * <p>
	 * Method under test:getBatteryLevel(), rotate(), jump(), getCurrentPosition(), getCurrentDirection()
	 * <p>
	 * Correct behavior: The starting point is (4,0), when the robot jumped through the wall, the current position is (3,0)
	 * The battery level decreased by 40. 
	 */
	@Test
	public final void testJump() throws Exception {		
		
		//starting point
		assertEquals(robot.getCurrentPosition()[0],4);  
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(CardinalDirection.East,robot.getCurrentDirection());
		assertTrue(robot.getBatteryLevel() == 3500f);

		//rotate and jump through the wall
		robot.rotate(Turn.AROUND);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.West);
		robot.jump();
		assertEquals(robot.getCurrentPosition()[0],3);
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.West);
		assertTrue(robot.getBatteryLevel() == 3454f);
	
	}

	
	/**
	 * Test case: Check if the distanceToObstacle method is working properly 
	 * <p>
	 * Method under test:getBatteryLevel(), move(), getCurrentPosition(), getCurrentDirection(), getOdometerReading()
	 * <p>
	 * Correct behavior: Moved the robot by 5 steps. Check its distances to walls of four different directions
	 * 
	 */
	@Test
	public final void testDistanceToObstacle() throws Exception{
	
	
		//starting point
		assertEquals(robot.getOdometerReading(),0);	
		assertEquals(robot.getCurrentPosition()[0],4);  
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(CardinalDirection.East,robot.getCurrentDirection());
		assertTrue(robot.getBatteryLevel() == 3500f);
		assertEquals(robot.distanceToObstacle(Direction.BACKWARD), 0);
		//move 5 steps
		robot.move(5);
		assertEquals(robot.getOdometerReading(),5);
		assertEquals(robot.distanceToObstacle(Direction.BACKWARD), 5);
		assertEquals(robot.distanceToObstacle(Direction.FORWARD), 6);
		assertEquals(robot.distanceToObstacle(Direction.RIGHT), 0);
		assertEquals(robot.distanceToObstacle(Direction.LEFT), 0);
		
		
	}
	
	
	/**
	 * Test case: Check if the IsAtExit method is working properly 
	 * <p>
	 * Method under test:getBatteryLevel(), move(), jump(), rotate(), 
	 * getCurrentPosition(), getCurrentDirection(), getOdometerReading(),isAtExit()
	 * <p>
	 * Correct behavior: Moved the robot to the exit manually, then check if it is at the exit
	 * 
	 */
	@Test
	public final void testIsAtExit() throws Exception{
		
	
		//starting point
		assertEquals(robot.getOdometerReading(),0);	
		assertEquals(robot.getCurrentPosition()[0],4); 
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(CardinalDirection.East,robot.getCurrentDirection());
		assertTrue(robot.getBatteryLevel() == 3500f);
		
		//test if at exit
		assertFalse(robot.isAtExit());

		//move to find exit
		robot.rotate(Turn.AROUND);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.West);
		robot.jump();
		assertEquals(robot.getCurrentPosition()[0],3);
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.West);
		assertTrue(robot.getBatteryLevel() == 3454f);
		
		robot.move(4);
		assertEquals(robot.getCurrentPosition()[0],0);
		assertEquals(robot.getCurrentPosition()[1],0);
		robot.rotate(Turn.LEFT);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.South);
		
		robot.move(3);
		assertEquals(robot.getCurrentPosition()[0],0);
		assertEquals(robot.getCurrentPosition()[1],3);
		assertTrue(robot.isAtExit());
		
	}
	

	/**
	 * Test case: Check if the CanSeeThroughTheExitIntoEternity() method is working properly 
	 * <p>
	 * Method under test:getBatteryLevel(), move(), jump(), rotate(), 
	 * getCurrentPosition(), getCurrentDirection(), getOdometerReading(), CanSeeThroughTheExitIntoEternity()
	 * <p>
	 * Correct behavior: Moved the robot to the exit manually, then check if it can see the exit
	 * 
	 */
	@Test
	public final void testCanSeeThroughTheExitIntoEternity() throws Exception {
		
		//starting point
		assertEquals(robot.getOdometerReading(),0);	
		assertEquals(robot.getCurrentPosition()[0],4); 
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(CardinalDirection.East,robot.getCurrentDirection());
		assertTrue(robot.getBatteryLevel() == 3500f);
		
		//test if can see exit
		assertFalse(robot.canSeeThroughTheExitIntoEternity(Direction.FORWARD));

		//move to find exit
		robot.rotate(Turn.AROUND);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.West);
		robot.jump();
		assertEquals(robot.getCurrentPosition()[0],3);
		assertEquals(robot.getCurrentPosition()[1],0);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.West);
		
		
		robot.move(4);
		assertEquals(robot.getCurrentPosition()[0],0);
		assertEquals(robot.getCurrentPosition()[1],0);
		robot.rotate(Turn.LEFT);
		assertEquals(robot.getCurrentDirection(),CardinalDirection.South);
		robot.move(3);
		assertEquals(robot.getCurrentPosition()[0],0);
		assertEquals(robot.getCurrentPosition()[1],3);
		assertTrue(robot.canSeeThroughTheExitIntoEternity(Direction.RIGHT));

		
		
	}
	
	/**
	 * Test case: Check if the IsInRoom() method is working properly 
	 * <p>
	 * Method under test:getBatteryLevel(), move(), jump(), rotate(), IsInRoom()
	 * <p>
	 * Correct behavior: Moved the robot in a room manually, then check if it is in the room.
	 * 
	 */
	@Test
	public final void testIsInRoom() throws Exception {  
	  
	  assertFalse(robot.isInsideRoom());
	  robot.move(11);
	  robot.rotate(Turn.RIGHT);
	  robot.move(4);
	  robot.rotate(Turn.LEFT);
	  robot.move(2);
	  assertTrue(robot.isInsideRoom());
	  robot.move(1);
	  assertTrue(robot.isInsideRoom());

	 
	 }
	
	
}


