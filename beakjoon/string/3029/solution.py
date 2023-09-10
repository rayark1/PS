# 현재 시간 입력 받기
current_time_str = input()
current_time_parts = current_time_str.split(':')
current_hour, current_minute, current_second = map(int, current_time_parts)

# 나트륨을 던질 시간 입력 받기
throw_time_str = input()
throw_time_parts = throw_time_str.split(':')
throw_hour, throw_minute, throw_second = map(int, throw_time_parts)

# 현재 시간과 나트륨을 던질 시간을 초로 변환
current_seconds = current_hour * 3600 + current_minute * 60 + current_second
throw_seconds = throw_hour * 3600 + throw_minute * 60 + throw_second

# 정인이가 기다려야 하는 시간 계산
if current_seconds < throw_seconds:
    wait_seconds = throw_seconds - current_seconds
else:
    wait_seconds = 24 * 3600 - (current_seconds - throw_seconds)

# 결과 출력
wait_hours = wait_seconds // 3600
wait_minutes = (wait_seconds % 3600) // 60
wait_seconds = wait_seconds % 60
wait_time_str = f"{wait_hours:02d}:{wait_minutes:02d}:{wait_seconds:02d}"
print(wait_time_str)