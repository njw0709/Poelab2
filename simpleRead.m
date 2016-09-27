function data = simpleRead()        
hold all; 
ser = serial('COM5');                             % this is the port the Ardunio is on
set(ser, 'BaudRate', 9600, 'Timeout', 0.005);     % 9600 is the serial intializing port, timeout is the max time to wait for data
fopen(ser);                                       % open the serial reader

finishup = onCleanup(@() cleanup(ser));           % removes remaining data from the serial reader                                                                                            
    function cleanup(s)
        fclose(s);                                % close the serial reader
        delete(s);                                % delete all information stored in the serial
        clear s                                   % remove data from MATLAB
        disp('Clean!')                            % tells you it cleaned: if it doesn't unplug and replug arduino
    end

fscanf(ser)                                             % pulls data from serial text file

while(true)
    if(get(ser, 'BytesAvailable') >= 1)                 % if there is data coming in from the arduino
        value = sscanf(fscanf(ser), '%d,%u,%d');        % sscanf reads formatted data from string, fscanf reads data from the text file (look up uses of %d and %u and %f)
        if (value == -1)                                % if the Ardunio prints -1 (you can change this case if you ned to!) , the scanning is done...  
            break                                       % ... so you end the loop
        else                                            % if scanning is still going                                        
            data(value(1),value(2)) = value(3);         % this is where you decide what to do with the data you are importing 
        end
    end
end

% Here is where you do any coordinate math you need to do
% and plot the data! 

end


