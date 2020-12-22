package generation;

import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.Before;
import org.junit.jupiter.api.Test;

import generation.Order.Builder;

public class MazeBuilderEllerTest {
	
	private MazeFactory factory;
	private StubOrder stub;
	
	
	/* Pseudocode for MazeFatoryTest
	 * 
	 * Tests for mazes generated with Eller's Algorithms 
	 * 
	 * 1. testRoom() 
	 * 
	 * - Method under test: stub.getMaze().getFloorplan().isInRoom(x,y)
	 * 
	 * - Use for loops to go through each cell, use stub.getMaze().getFloorplan().isInRoom(x,y)
	 *   to check if there exist at least one cells that is in room
	 * 
	 * - Correct behavior: If there's at least one cell is in room, pass
	 * 
	 * 
	 * 2. testNoRoomForLevel0()
	 * 
	 * - Method under test: stub.getMaze().getFloorplan().isInRoom(x,y)
	 * 
	 * - Use for loops to go through each cell, use stub.getMaze().getFloorplan().isInRoom(x,y) 
	 *   to check if there's no cell that is in room for level 0's maze 
	 * 
	 * - Correct behavior: If there's no cell that is in room, pass
	 * 
	 * 
	 */
	
	
	
	public void setup() {
		factory = new MazeFactory();
		stub = new StubOrder(Builder.Eller, 1, true);
		assertNotNull(factory);
		assertNotNull(stub);
	}
	
	
	/**
	 * Test case: Check if the starting point is the point that has maximum 
	 * distance to the exit.
	 * <p>
	 * Method under test: stub.getMaze.getDistanceToExit(x,y)
	 * <p>
	 * Correct behavior: The indices of the point that has maximum distance
	 * match the x, y values of the starting point.
	 */
	
	@Test
	public void testMaximumDistancetoExit() {
		setup();
		factory.order(stub);
		factory.waitTillDelivered();
		int d;
		int temp_x = 0;
		int temp_y = 0;
		d = 0;
		for(int x = 0; x < stub.getMaze().getWidth(); x++) {
			for(int y = 0; y < stub.getMaze().getHeight(); y++) {
				if(stub.getMaze().getDistanceToExit(x, y) > d) {
					d = stub.getMaze().getDistanceToExit(x, y);
					temp_x = x;
					temp_y = y;
					
					
				}
			}
		}
		int[] array = stub.getMaze().getStartingPosition();
		assertEquals(temp_x, array[0]);
		assertEquals(temp_y, array[1]);
		
		
	}
	

	/**
	 * Test case: Check if the generated maze has only one exit
	 * <p>
	 * Method under test: DFS, stub.getMaze.isExitPosition(x,y)
	 * <p>
	 * Correct behavior: There's only one exit for this maze.
	 */
	@Test
	public void testOneExit() {
		setup();
		factory.order(stub);
		factory.waitTillDelivered();
		
	
		int c = 0;
		for(int x = 0; x < stub.getMaze().getWidth(); x++) {
			for(int y = 0; y < stub.getMaze().getHeight(); y++) {
				if(stub.getMaze().getFloorplan().isExitPosition(x,y) == true) {
						c++;
					
				}
			}
		}
		assertEquals(1,c);
	
	}
	
	
	/**
	 * Test case: Check if the exit is reachable
	 * <p>
	 * Method under test: Eller, stub.getMaze().getDistanceToExit(x, y)
	 * <p>
	 * Correct behavior: The distance to exit equals infinity.
	 */
	@Test
	public void testExitisReachable() {
		setup();
		factory.order(stub);
		factory.waitTillDelivered();
		

		int c = 0;
		for(int x = 0; x < stub.getMaze().getWidth(); x++) {
			for(int y = 0; y < stub.getMaze().getHeight(); y++) {
				if(stub.getMaze().getDistanceToExit(x, y) == generation.Distance.INFINITY) {
						c++;
					
				}
			}
		}
		assertEquals(0,c);
	}
	

	/**
	 * Test case: Check if there's at least one room in the maze 
	 * <p>
	 * Method under test: Eller, stub.getMaze().getFloorplan().hasNoWall(x, y, CardinalDirection.North) 
	 * <p>
	 * Correct behavior: There exists a cell that has no wall in four directions 
	 */
	@Test
	public void testRoom() {
		factory = new MazeFactory();
		stub = new StubOrder(Builder.Eller, 5, false);
		factory.order(stub);
		factory.waitTillDelivered();
		
		boolean temp = false;
		
		for(int x = 1; x < stub.getMaze().getWidth()-1; x++) {
			for(int y = 1; y < stub.getMaze().getHeight()-1; y++) {
				if (stub.getMaze().getFloorplan().isInRoom(x,y)) {
					temp = true;
					break;
				}
//				if (stub.getMaze().getFloorplan().hasNoWall(x, y, CardinalDirection.South) 
//						&& stub.getMaze().getFloorplan().hasNoWall(x, y, CardinalDirection.North) 
//						&& stub.getMaze().getFloorplan().hasNoWall(x, y, CardinalDirection.West)
//						&& stub.getMaze().getFloorplan().hasNoWall(x, y, CardinalDirection.East)) {
//					temp = true;
//					//break;
//				}
					
			}
		
		}
			
		assertEquals(true,temp);
	}

	/**
	 * Test case: Check if there's no room in the level 0 maze
	 * <p>
	 * Method under test: Eller, stub.getMaze().getFloorplan().isInRoom(x,y)
	 * <p>
	 * Correct behavior: There does not exist a cell that is in room.
	 */
	@Test
	public void testNoRoomForLevel0() {
		factory = new MazeFactory();
		stub = new StubOrder(Builder.Eller, 0, true);
		factory.order(stub);
		factory.waitTillDelivered();
		
		boolean temp = false;
		for(int x = 1; x < stub.getMaze().getWidth()-1; x++) {
			for(int y = 1; y < stub.getMaze().getHeight()-1; y++) {
				if (stub.getMaze().getFloorplan().isInRoom(x,y)) {
					temp = true;
					break;
				}
					
			}
		
		}
		assertEquals(false,temp);
	}
	
	
	
	
}