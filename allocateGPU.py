def allocateGPU(allocateGPU):
    '''
    :param allocateGPU: (int) 4096 # 1 GB --> 1024  MB
    :return: None

    # GPUs --> [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
    # GPUs --> []

    # Reference: https://www.tensorflow.org/guide/gpu
    '''

    GPUs = tf.config.experimental.list_physical_devices('GPU')

    if GPUs:
        try:
            tf.config.experimental.set_virtual_device_configuration(GPUs[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=allocateGPU)])
        except RuntimeError:
            print(RuntimeError)
    else:
        print('No GPU detected!')
#end-def


####################################################
allocateGPU(4096) # allocateGPU (MB): 4 GB --> 4096.
####################################################
