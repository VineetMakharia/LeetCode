class Solution:
	def critical_connections(self,n,edges):
		from collections import defaultdict
		graph = defaultdict(list)
		ans = []
		for e1,e2 in edges:
			graph[e1].append(e2)
			graph[e2].append(e1)

		initial_time = [-1]*n
		lowest_time = [-1]*n

		def dfs(current,parent,time):
			print("IT",initial_time)
			print("LT",lowest_time)
			time+=1
			initial_time[current]=time
			lowest_time[current]=time
			for nei in graph[current]:
				if nei==parent:
					continue
				if initial_time[nei]==-1:
					dfs(nei,current,time)
					if initial_time[nei]==lowest_time[nei]:
						ans.append([current,nei])
				lowest_time[current] = min(lowest_time[nei],lowest_time[current])

		dfs(0,0,0)
		print("IT",initial_time)
		print("LT",lowest_time)
		return ans

obj = Solution()
# print(obj.critical_connections(4,[[0,1],[1,2],[2,0],[1,3]]))
print(obj.critical_connections(3,[[0,1],[1,2]]))
