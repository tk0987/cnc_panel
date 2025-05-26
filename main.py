# kinda easy i hope
import _thread
import main1
import main2


_thread.start_new_thread(main2.core1_task, ())

main1.core0_task()

