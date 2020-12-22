package edu.wm.cs.cs301.game2048;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class State implements GameState {

	
	int[] myarray = new int[16];
	
	public State(State currentState) {
		// TODO Auto-generated constructor stub
		this.myarray = new int[16];
		for (int i=0;i<16;i++) {
			this.myarray[i] = currentState.myarray[i];
		}
	}

	public State() {
		// TODO Auto-generated constructor stub
	}

	@Override
	public int getValue(int x, int y) {
		// TODO Auto-generated method stub
		return myarray[y*4+x];
	}

	@Override
	public void setValue(int x, int y, int value) {
		// TODO Auto-generated method stub
		myarray [y*4+x] = value;

	}

	@Override
	public void setEmptyBoard() {
		// TODO Auto-generated method stub
		for (int i = 0; i<4; i++) {
			for (int j=0; j<4; j++) {
				setValue(i,j,0);
			}
		}

	}

	@Override
	public boolean addTile() {
		// TODO Auto-generated method stub
		if (isFull() == true) {
			return false;
		}
		else {
			
			ArrayList<Integer> emptytile = new ArrayList<Integer>();
			for (int i = 0; i<4; i++) {
				for (int j = 0; j<4; j++) {
					if (this.getValue(i,j) == 0) {emptytile.add(j*4+i);}
				}
			}
			Random rand = new Random();
			int index = rand.nextInt(emptytile.size()); 
			int x = emptytile.get(index) % 4;
			int y = emptytile.get(index) / 4;
			Random rand_2 = new Random();
			int temp = rand_2.nextInt(10); 
			if (temp < 9) {
				setValue(x,y,2);
			}else{
				setValue(x,y,4);
			}
			
			return true;
		}
	}

	
	@Override
	public boolean isFull() {
		// TODO Auto-generated method stub
		int count = 0;
		for (int i = 0; i<4; i++) {
			for (int j = 0; j<4; j++) {
				if (getValue(i,j) == 0)
					count ++;
			}
		}
		if (count != 0) return false;
		else 
			return true;
	}

	@Override
	public boolean canMerge() {
		// TODO Auto-generated method stub
		ArrayList<Integer> tiles = new ArrayList<Integer>();
		for (int i = 0; i<4; i++) {
			for (int j = 0; j<4; j++) {
				if (getValue(i,j) != 0) {
					tiles.add(j*4+i);
				}
			}
		}
		for (int a = 0; a< tiles.size();a++) {
			for (int b=a+1; b<tiles.size();b++) {
				int a_x = tiles.get(a)%4;
				int b_x = tiles.get(b)%4;
				int a_y = tiles.get(a)/4;
				int b_y = tiles.get(b)/4;
						
				if (((a_x == b_x && (a_y-b_y==1 || b_y-a_y==1)) || (a_y == b_y && (a_x-b_x==1 || b_x-a_x==1))) 
						&& getValue(a_x,a_y) == getValue(b_x,b_y)) {
					return true;
				}
					
			}
		
		}
	
		return false;
	}

	@Override
	public boolean reachedThreshold() {
		// TODO Auto-generated method stub
		for (int i = 0; i<4; i++) {
			for (int j = 0; j<4; j++) {
				if (getValue(i,j) >= 2048)
					return true;
			}
		}
				return false;
	}

	
	private void compress() {

		
		
		for (int y=0; y<4; y++) {
			for (int x=0; x<3; x++) {
			
				if (getValue(x,y)!= 0){;}

				if (getValue(x,y) == 0) {
					int current = x;
					while (getValue(x+1,y) == 0){
						if (x == 2) {
							break;
						}
						x++;	
					}
				
					if (x!=3) {
						setValue(current,y,getValue(x+1,y));
						setValue(x+1,y,0);
						x = current;
					}
				}
			}
			
		}
	}
		
		
	private int merge() {
		
		int scores = 0;
		for (int y=0;y<4;y++) {
			int merge = 0;
			ArrayList<Integer> cells = new ArrayList<Integer>();
			
			for(int x=0; x<3;x++) {
				if ((getValue(x,y) == getValue(x+1,y)) 
						&& (getValue(x,y) != 0) && (getValue(x+1,y)!= 0)) {
					cells.add(x);
					x++;
					merge++;
				
				}
			}
			
			if (merge == 0){;}
			if (merge == 1) {
				int index = cells.get(0);
				scores = scores +  2*getValue(index,y);
				setValue(index,y,2*getValue(index,y));
				setValue(index+1,y,0);
			}
			if (merge == 2) {
				scores = scores + 2*getValue(0,y);
				setValue(0,y,2*getValue(0,y));
				setValue(1,y,0);
				scores = scores +  2 * getValue(2,y);
				setValue(2,y,2*getValue(2,y));
				setValue(3,y,0);
			}
		}
		
		return scores;
		
			
	}
	
	private void rotateLeft() {
		
		
		int [] left = new int[16];
		Arrays.fill(left, 0);
		  
		   
		for (int x = 0; x<4; x++) {
			for(int y = 0; y<4; y++) {
				left[4*(4-x-1)+y] = getValue(x,y);
			}
		}
		  
		for (int x = 0; x<4; x++) {
			for(int y = 0; y<4; y++) {
				myarray[y*4+x] = left[y*4+x];
			}
		}
	}
	
	
	private void rotateRight() {
		
		
		int [] right = new int[16];
		Arrays.fill(right, 0);
		  
		   
		for (int x=0; x<4; x++) {
			for(int y=0; y<4; y++) {
				right[4*x + (4-y-1)] = getValue(x,y);
			}
		}
		  
		for (int x=0; x<4; x++) {
			for (int y=0; y<4; y++) {
				myarray[y*4+x] = right[y*4+x];
				
			}
		}
	}
	
	@Override
	public int left() {
		// TODO Auto-generated method stub
		compress();
		int scores = merge();
		compress();


		return scores;
	}

	@Override
	public int right() {
		// TODO Auto-generated method stub
		rotateLeft();
		rotateLeft();
		compress();
		int scores = merge();
		compress();
		rotateRight();
		rotateRight();
		return scores;
	}

	@Override
	public int down() {
		// TODO Auto-generated method stub
		rotateRight();
		compress();
		int scores = merge();
		compress();
		rotateLeft();
		return scores;
	}

	@Override
	public int up() {
		// TODO Auto-generated method stub
		rotateLeft();
		compress();
		int scores = merge();
		compress();
		rotateRight();
		return scores;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + Arrays.hashCode(myarray);
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		State other = (State) obj;
		if (!Arrays.equals(myarray, other.myarray))
			return false;
		return true;
	}
	
	

}
